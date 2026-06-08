import hashlib
import math
import random
from fractions import Fraction

from core.tasks import get_task_for_skill


def difficulty_from_mastery(mastery):
    if mastery < 0.4:
        return "easy"
    if mastery < 0.7:
        return "medium"
    return "hard"


def fraction_or_decimal(value):
    if isinstance(value, Fraction):
        return str(value)
    if int(value) == value:
        return str(int(value))
    return str(round(value, 3))


def accepted_numeric(value):
    if isinstance(value, Fraction):
        decimal = float(value)
        return f"{value}|{round(decimal, 2)}|{round(decimal, 3)}|{round(decimal, 4)}"
    return f"{value}|{float(value)}"


def make_task(title, latex, text, answer, accepted, hint, difficulty):
    return {
        "difficulty": difficulty,
        "task_title": title,
        "task_latex": latex,
        "task_text": text,
        "expected_answer": answer,
        "accepted_answers": accepted,
        "hint": hint,
    }


def generated_task_for_skill(tasks_df, skill_id, mastery, seed, skill_title=None):
    stable_hash = int(hashlib.md5(skill_id.encode("utf-8")).hexdigest()[:8], 16)
    rng = random.Random(seed + stable_hash)
    difficulty = difficulty_from_mastery(mastery)

    generators = {
        # ── Arithmetic / Algebra ──────────────────────────────────────────────
        "arithmetic":              generate_arithmetic,
        "fractions":               generate_fractions,
        "simplify_expression":     generate_simplify_expression,
        "simplify_polynomial":     generate_simplify_polynomial,
        "solve_linear_equation":   generate_solve_linear_equation,
        "quadratic_equation":      generate_quadratic_equation,
        "factoring_quadratic":     generate_factoring_quadratic,
        "system_of_equations":     generate_system_of_equations,
        "linear_inequality":       generate_linear_inequality,
        "absolute_value_eq":       generate_absolute_value_eq,
        "exponent_rules":          generate_exponent_rules,
        "polynomial_evaluation":   generate_polynomial_evaluation,

        # ── Functions ─────────────────────────────────────────────────────────
        "function_notation":       generate_evaluate_function,
        "substitution":            generate_substitution,
        "evaluate_function":       generate_evaluate_function,
        "sign_of_function":        generate_sign_of_function,
        "logarithm_basic":         generate_logarithm_basic,
        "exponential_evaluate":    generate_exponential_evaluate,
        "trig_evaluate":           generate_trig_evaluate,
        "inverse_function_value":  generate_inverse_function_value,
        "composite_function":      generate_composite_function,

        # ── Calculus ──────────────────────────────────────────────────────────
        "power_rule":              generate_power_rule,
        "polynomial_derivative":   generate_polynomial_derivative,
        "evaluate_derivative":     generate_evaluate_derivative,
        "chain_rule":              generate_chain_rule,
        "product_rule":            generate_product_rule,
        "quotient_rule":           generate_quotient_rule,
        "limit_polynomial":        generate_limit_polynomial,
        "power_rule_integral":     generate_power_rule_integral,
        "definite_integral":       generate_definite_integral,

        # ── Root finding ──────────────────────────────────────────────────────
        "root_concept":            generate_root_concept,
        "check_sign_change":       generate_check_sign_change,
        "midpoint_formula":        generate_midpoint,
        "interval_update":         generate_interval_update,
        "bisection_step":          generate_bisection_step,
        "fixed_point_formula":     generate_fixed_point_formula,
        "fixed_point_step":        generate_fixed_point_step,
        "contraction_check":       generate_contraction_check,
        "newton_formula":          generate_newton_formula_application,
        "newton_step":             generate_newton_step,
        "newton_iteration":        generate_newton_second_step,

        # ── Linear Algebra ────────────────────────────────────────────────────
        "matrix_entry":            generate_matrix_entry,
        "matrix_vector_product":   generate_matrix_vector_product,
        "matrix_norm":             generate_matrix_norm,
        "diagonal_dominance":      generate_diagonal_dominance,
        "determinant_2x2":         generate_determinant_2x2,
        "eigenvalue_2x2":          generate_eigenvalue_2x2,
        "dot_product":             generate_dot_product,
        "vector_norm":             generate_vector_norm,
        "linear_combination":      generate_linear_combination,

        # ── PageRank ──────────────────────────────────────────────────────────
        "directed_graph":          generate_outdegree,
        "outdegree":               generate_outdegree,
        "graph_degree":            generate_outdegree,
        "distribute_weight":       generate_distribute_weight,
        "transition_matrix":       generate_transition_entry,
        "column_stochastic":       generate_column_sum,
        "power_iteration":         generate_power_iteration,
        "pagerank_step":           generate_pagerank_step,

        # ── Interpolation / Splines ───────────────────────────────────────────
        "polynomial_form":                  generate_polynomial_form,
        "vandermonde_matrix":               generate_vandermonde_row,
        "lagrange_basis":                   generate_lagrange_basis_value,
        "lagrange_polynomial":              generate_lagrange_term,
        "piecewise_function":               generate_spline_pieces,
        "first_derivative_continuity":      generate_first_derivative_continuity,
        "second_derivative_continuity":     generate_second_derivative_continuity,
        "natural_boundary":                 generate_natural_boundary,
        "natural_spline":                   generate_spline_pieces,

        # ── Regression ────────────────────────────────────────────────────────
        "linear_regression_fit":   generate_linear_regression_fit,

        # ── Discrete Mathematics ──────────────────────────────────────────────
        "set_operation":           generate_set_operation,
        "set_cardinality":         generate_set_cardinality,
        "logic_truth_value":       generate_logic_truth_value,
        "big_o_comparison":        generate_big_o_comparison,
        "recurrence_step":         generate_recurrence_step,
        "combinatorics_basic":     generate_combinatorics_basic,

        # ── Extra ─────────────────────────────────────────────────────────────
        "slope_from_points":       generate_slope_from_points,
        "foil_binomials":          generate_foil_binomials,
        "distributive_property":   generate_distributive_property,
        "percent_problem":         generate_percent_problem,
        "arithmetic_sequence":     generate_arithmetic_sequence,
        "geometric_sequence":      generate_geometric_sequence,
        "complex_arithmetic":      generate_complex_arithmetic,
    }

    generator = generators.get(skill_id)
    if generator is None:
        generator = generators.get(resolve_generator_key(skill_id, skill_title, rng))

    if generator is None:
        return get_task_for_skill(tasks_df, skill_id, mastery, seed=seed + stable_hash)

    return generator(rng, difficulty)


def resolve_generator_key(skill_id, skill_title, rng):
    # Use title as the primary signal; fall back to skill_id tail only if title is absent.
    # Never use the full skill_id (it contains cluster names that cause false matches).
    t = (skill_title or skill_id.split("skill_", 1)[-1].replace("_", " ")).lower()

    # ── Numerical methods ──────────────────────────────────────────────────────
    if "bisection" in t:
        return rng.choice(["bisection_step", "check_sign_change", "interval_update", "midpoint_formula"])
    if "fixed point" in t or "fixed-point" in t:
        return rng.choice(["fixed_point_formula", "fixed_point_step", "contraction_check"])
    if "newton" in t and ("method" in t or "step" in t or "root" in t or "raphson" in t or "numerically" in t):
        return rng.choice(["newton_step", "newton_iteration", "newton_formula"])
    if "secant method" in t:
        return rng.choice(["newton_step", "newton_formula"])
    if "contraction" in t:
        return "contraction_check"
    if "convergence rate" in t or "compare convergence" in t:
        return "big_o_comparison"
    if "regression" in t or "least squares" in t:
        return "linear_regression_fit"
    if "pagerank" in t or "page rank" in t:
        return rng.choice(["pagerank_step", "transition_matrix", "column_stochastic", "power_iteration"])
    if "transition matrix" in t or "stochastic" in t:
        return rng.choice(["transition_matrix", "column_stochastic"])
    if "power iteration" in t or "power method" in t:
        return "power_iteration"
    if "interpolat" in t or "lagrange" in t or "vandermonde" in t or "divided difference" in t:
        return rng.choice(["polynomial_form", "vandermonde_matrix", "lagrange_basis", "lagrange_polynomial"])
    if "spline" in t or "piecewise" in t or "cubic spline" in t:
        return rng.choice([
            "piecewise_function",
            "first_derivative_continuity",
            "second_derivative_continuity",
            "natural_boundary",
        ])
    if "trapezoidal" in t:
        return "definite_integral"
    if "simpson" in t:
        return "definite_integral"
    if "euler method" in t or "runge" in t:
        return "recurrence_step"
    if "finite difference" in t:
        return "polynomial_derivative"
    if "estimate derivative" in t:
        return "evaluate_derivative"
    if "numerical stability" in t or "condition number" in t:
        return "matrix_norm"
    if "lu decomposition" in t or "gaussian elimination" in t or "row echelon" in t:
        return rng.choice(["matrix_entry", "matrix_vector_product", "matrix_norm"])
    if "jacobi" in t or "gauss-seidel" in t or "gauss seidel" in t:
        return rng.choice(["matrix_vector_product", "matrix_norm"])

    # ── Linear Algebra ─────────────────────────────────────────────────────────
    if "determinant" in t:
        return "determinant_2x2"
    if "eigenvalue" in t or "eigenvector" in t or "characteristic polynomial" in t or "eigenspace" in t or "diagonaliz" in t:
        return "eigenvalue_2x2"
    if "dot product" in t or "inner product" in t or "scalar product" in t:
        return "dot_product"
    if "projection" in t or "orthogonality" in t or "gram-schmidt" in t or "orthogonal" in t:
        return "dot_product"
    if "norm" in t and ("vector" in t or "compute" in t or "matrix" in t):
        return rng.choice(["vector_norm", "matrix_norm"])
    if "singular value" in t or "svd" in t or "qr decomposition" in t:
        return rng.choice(["eigenvalue_2x2", "matrix_vector_product"])
    if "linear combination" in t or "span" in t or "linear independence" in t or "find a basis" in t or "compute dimension" in t:
        return "linear_combination"
    if "subspace" in t or "null space" in t or "column space" in t or "rank" in t:
        return rng.choice(["matrix_norm", "system_of_equations"])
    if "linear transformation" in t or "change basis" in t:
        return "matrix_vector_product"
    if ("matrix" in t or "transpose" in t or "matrix-vector" in t or "matrix vector" in t or
            "identity matrix" in t or "inverse matrix" in t):
        return rng.choice(["matrix_entry", "matrix_vector_product", "matrix_norm"])
    if "vector" in t and ("add" in t or "scale" in t or "subtract" in t or "component" in t):
        return "linear_combination"
    if "adjacency matrix" in t:
        return "matrix_entry"

    # ── Calculus ───────────────────────────────────────────────────────────────
    if "chain rule" in t:
        return "chain_rule"
    if "product rule" in t:
        return "product_rule"
    if "quotient rule" in t:
        return "quotient_rule"
    if "fundamental theorem" in t:
        return "definite_integral"
    if "riemann sum" in t:
        return "arithmetic"
    if "definite integral" in t or "area under" in t or "area between" in t:
        return "definite_integral"
    if "improper integral" in t:
        return "definite_integral"
    if "integrat" in t or "antideriv" in t or "substitution rule" in t or "integration by parts" in t:
        return rng.choice(["power_rule_integral", "definite_integral"])
    if "trigonometric integral" in t or "trigonometric substitution" in t:
        return "trig_evaluate"
    if "partial fraction" in t:
        return "fractions"
    if "volume" in t or "arc length" in t or "work from force" in t or "surface integral" in t:
        return "definite_integral"
    if "double integral" in t or "triple integral" in t or "polar coordinates" in t:
        return "definite_integral"
    if "taylor" in t or "maclaurin" in t or "power series" in t:
        return "polynomial_evaluation"
    if "taylor polynomial" in t or "taylor series" in t:
        return "polynomial_evaluation"
    if "radius of convergence" in t or "ratio test" in t or "root test" in t or "divergence test" in t or "comparison test" in t or "integral test" in t:
        return "recurrence_step"
    if "geometric series" in t or "sequence convergence" in t:
        return rng.choice(["recurrence_step", "geometric_sequence"])
    if "limit" in t:
        return "limit_polynomial"
    if "implicit differentiation" in t or "related rates" in t:
        return "chain_rule"
    if "tangent line" in t or "linear approximation" in t:
        return "evaluate_derivative"
    if "critical point" in t or "increasing and decreasing" in t or "first derivative test" in t or "second derivative test" in t:
        return "evaluate_derivative"
    if "optimization problem" in t:
        return "evaluate_derivative"
    if "derivative" in t or "differentiat" in t:
        return rng.choice(["power_rule", "polynomial_derivative", "evaluate_derivative"])
    if "rate of change" in t:
        return "polynomial_derivative"
    if "partial derivative" in t or "gradient vector" in t or "directional derivative" in t:
        return "polynomial_derivative"
    if "multivariable function" in t or "level curve" in t or "tangent plane" in t:
        return "evaluate_function"
    if "lagrange multiplier" in t:
        return "system_of_equations"
    if "constrained optimization" in t or "convex" in t or "stationary point" in t or "optimality" in t:
        return rng.choice(["evaluate_derivative", "system_of_equations"])
    if "gradient descent" in t:
        return "evaluate_derivative"
    if "objective function" in t:
        return "evaluate_function"
    if "green" in t and "theorem" in t or "divergence theorem" in t or "stokes" in t:
        return "definite_integral"
    if "line integral" in t or "conservative vector" in t:
        return "definite_integral"
    if "parametric" in t or "polar equation" in t:
        return rng.choice(["trig_evaluate", "chain_rule"])
    if "cylindrical" in t or "spherical" in t:
        return "trig_evaluate"
    if "laplace transform" in t:
        return "polynomial_evaluation"

    # ── Differential Equations ─────────────────────────────────────────────────
    if "separable equation" in t or "integrating factor" in t or "first-order" in t or "first order ode" in t:
        return rng.choice(["power_rule_integral", "definite_integral"])
    if "slope field" in t:
        return "evaluate_derivative"
    if "homogeneous" in t and "coefficient" in t:
        return "quadratic_equation"
    if "undetermined coefficient" in t or "variation of parameter" in t:
        return "polynomial_derivative"
    if "initial value" in t:
        return "definite_integral"
    if "eigenvalue" in t and ("system" in t or "ode" in t):
        return "eigenvalue_2x2"
    if "stability" in t and "equilibri" in t:
        return "evaluate_derivative"
    if "differential equation" in t:
        return rng.choice(["polynomial_derivative", "definite_integral"])

    # ── Algebra / Algebra I ────────────────────────────────────────────────────
    if "quadratic formula" in t:
        return "quadratic_equation"
    if "complete the square" in t or "vertex of a parabola" in t:
        return rng.choice(["quadratic_equation", "factoring_quadratic"])
    if "quadratic" in t or "parabola" in t:
        return rng.choice(["quadratic_equation", "factoring_quadratic"])
    if "factor trinomial" in t or "factor greatest" in t or "factor difference" in t:
        return "factoring_quadratic"
    if "factor out" in t or "factor" in t and "common" in t:
        return "factoring_quadratic"
    if "polynomial identit" in t:
        return "polynomial_evaluation"
    if "multiply binomial" in t or "foil" in t:
        return "foil_binomials"
    if "multiply monomial" in t or "add and subtract polynomial" in t:
        return "simplify_polynomial"
    if "system" in t and ("equation" in t or "substitution" in t or "elimination" in t or "graphing" in t):
        return "system_of_equations"
    if "classify system" in t or "number of solution" in t:
        return "system_of_equations"
    if "inequalit" in t:
        return "linear_inequality"
    if "absolute value" in t:
        return "absolute_value_eq"
    if "slope" in t:
        return "slope_from_points"
    if "intercept" in t and ("x-" in t or "y-" in t or "write" in t or "identify" in t or "graph" in t):
        return "slope_from_points"
    if "slope-intercept" in t or "line equation" in t or "linear equation" in t or "linear form" in t:
        return rng.choice(["solve_linear_equation", "slope_from_points"])
    if "solve" in t and "equation" in t:
        return "solve_linear_equation"
    if "exponent rule" in t or "power of power" in t or "zero and negative exponent" in t:
        return "exponent_rules"
    if "evaluate power" in t or "evaluate exponential" in t:
        return "exponent_rules"
    if "square root" in t or "simplify radical" in t or "radical equation" in t or "irrational" in t:
        return rng.choice(["root_concept", "exponent_rules"])
    if "rational exponent" in t:
        return "exponent_rules"
    if "rational expression" in t or "rational equation" in t or "excluded value" in t:
        return "fractions"
    if "inverse variation" in t:
        return "fractions"
    if "distributive property" in t or "distribute" in t:
        return "distributive_property"
    if "combine like term" in t:
        return "simplify_expression"
    if "equivalent expression" in t or "create equivalent" in t:
        return rng.choice(["simplify_expression", "simplify_polynomial"])
    if "polynomial" in t:
        return rng.choice(["simplify_polynomial", "polynomial_evaluation"])
    if "fraction" in t:
        return "fractions"
    if "percent" in t:
        return "percent_problem"
    if "simplif" in t:
        return rng.choice(["simplify_expression", "simplify_polynomial"])
    if "whole number" in t or "place value" in t or "order of operation" in t or "arithmetic" in t:
        return "arithmetic"
    if "integer" in t or "rational number" in t or "number line" in t:
        return "arithmetic"

    # ── Functions ──────────────────────────────────────────────────────────────
    if "logarithm" in t or "log rule" in t or "natural log" in t or "log base" in t:
        return "logarithm_basic"
    if "solve exponential" in t or "solve logarithm" in t:
        return "logarithm_basic"
    if "exponential" in t and ("function" in t or "growth" in t or "decay" in t or "evaluate" in t):
        return "exponential_evaluate"
    if "unit circle" in t or "evaluate" in t and "trig" in t:
        return "trig_evaluate"
    if "sin" in t or "cos" in t or "tan" in t or "trigonometr" in t or "radian" in t or "degree" in t:
        return "trig_evaluate"
    if "de moivre" in t:
        return "trig_evaluate"
    if "inverse function" in t or "find inverse" in t:
        return "inverse_function_value"
    if "compose function" in t or "composition" in t:
        return "composite_function"
    if "transform" in t and ("function" in t or "parent" in t or "shift" in t or "reflection" in t or "stretch" in t):
        return rng.choice(["evaluate_function", "polynomial_evaluation"])
    if "function notation" in t or "evaluate function" in t or "evaluate" in t and "formula" in t:
        return "evaluate_function"
    if "domain" in t or "range" in t:
        return "evaluate_function"
    if "increasing" in t or "decreasing" in t or "maxima" in t or "minima" in t:
        return "evaluate_derivative"
    if "piecewise" in t or "sketch rational" in t:
        return "evaluate_function"
    if "asymptote" in t:
        return "fractions"
    if "arithmetic sequence" in t:
        return "arithmetic_sequence"
    if "geometric sequence" in t:
        return "geometric_sequence"
    if "sigma notation" in t or "finite series" in t or "sum" in t and "series" in t:
        return rng.choice(["arithmetic_sequence", "geometric_sequence"])

    # ── Complex numbers ────────────────────────────────────────────────────────
    if "complex" in t and ("arithmetic" in t or "add" in t or "multiply" in t or "divide" in t or
                           "conjugate" in t or "polar form" in t or "plane" in t):
        return "complex_arithmetic"
    if "complex" in t and "differentiab" in t:
        return "evaluate_derivative"
    if "cauchy-riemann" in t or "cauchy riemann" in t:
        return "complex_arithmetic"
    if "contour integral" in t or "cauchy integral" in t or "residue" in t or "laurent series" in t:
        return "complex_arithmetic"
    if "complex exponential" in t or "complex logarithm" in t:
        return "complex_arithmetic"

    # ── Discrete Mathematics ───────────────────────────────────────────────────
    if "permutation" in t or "multiplication principle" in t or "addition principle" in t:
        return "combinatorics_basic"
    if "combination" in t or "binomial coefficient" in t or "choose" in t:
        return "combinatorics_basic"
    if "inclusion-exclusion" in t or "inclusion exclusion" in t:
        return "set_cardinality"
    if "recurrence relation" in t or "recurrence" in t or "fibonacci" in t:
        return "recurrence_step"
    if "graph" in t and ("vertex" in t or "edge" in t or "degree" in t or "path" in t or "cycle" in t or
                         "tree" in t or "traversal" in t or "connected" in t):
        return rng.choice(["outdegree", "graph_degree"])
    if "represent graph" in t:
        return "outdegree"
    if "set" in t and ("element" in t or "operation" in t or "union" in t or "intersect" in t or
                       "venn" in t or "subset" in t or "partition" in t or "cartesian" in t):
        return rng.choice(["set_operation", "set_cardinality"])
    if "binary relation" in t or "properties of relation" in t or "order relation" in t or "equivalence relation" in t:
        return "logic_truth_value"
    if "function" in t and "formal" in t:
        return "evaluate_function"
    if "propositional" in t or "truth table" in t or "de morgan" in t or "tautology" in t or "logical implication" in t:
        return "logic_truth_value"
    if "big o" in t or "big-o" in t or "omega" in t or "theta notation" in t or "growth rate" in t:
        return "big_o_comparison"
    if "complexity" in t or "asymptot" in t or "algorithm" in t and "class" in t:
        return "big_o_comparison"
    if "p class" in t or "np class" in t or "p vs np" in t:
        return "big_o_comparison"

    # ── Proof and Math Language ────────────────────────────────────────────────
    if "direct proof" in t or "contrapositive" in t or "contradiction" in t or "proof" in t:
        return "logic_truth_value"
    if "mathematical induction" in t:
        return "recurrence_step"
    if "divisibility" in t:
        return "arithmetic"
    if "logical connective" in t or "quantified statement" in t or "logical" in t:
        return "logic_truth_value"
    if "set" in t and ("subset" in t or "work with" in t or "set operation" in t):
        return "set_operation"
    if "function" in t and "mapping" in t:
        return "evaluate_function"

    # ── Real Analysis ──────────────────────────────────────────────────────────
    if "epsilon" in t or "cauchy criterion" in t or "uniform continuity" in t:
        return "limit_polynomial"
    if "sequence convergence" in t or "subsequence" in t or "monotone convergence" in t:
        return "recurrence_step"
    if "mean value theorem" in t:
        return "evaluate_derivative"
    if "differentiability" in t or "rigorously" in t:
        return rng.choice(["evaluate_derivative", "limit_polynomial"])
    if "series convergence" in t or "uniform convergence" in t or "power series" in t and "rigorous" in t:
        return "recurrence_step"
    if "riemann integr" in t or "fundamental theorem rigorously" in t:
        return "definite_integral"

    # ── Abstract Algebra ───────────────────────────────────────────────────────
    if "group axiom" in t or "subgroup" in t or "coset" in t or "lagrange theorem" in t or "homomorphism" in t:
        return "combinatorics_basic"
    if "ring" in t or "ideal" in t or "field" in t or "module" in t:
        return "arithmetic"
    if "isomorphism" in t or "group action" in t or "quotient" in t:
        return "logic_truth_value"

    # ── Extra catch-all for plurals / edge cases ───────────────────────────────
    if "adjacen" in t:
        return "matrix_entry"
    if "powers of powers" in t or "zero and negative" in t or "exponent" in t:
        return "exponent_rules"
    if "substitution" in t or "substitut" in t:
        return "substitution"
    if "numerator" in t or "denominator" in t or "common denominator" in t:
        return "fractions"
    if "compare" in t and "number" in t or "order" in t and "number" in t:
        return "arithmetic"
    if "estimate" in t and "reasonab" in t:
        return "arithmetic"
    if "plot point" in t or "coordinate plane" in t:
        return "arithmetic"
    if "check a solution" in t or "model word problem" in t:
        return "system_of_equations"
    if "discriminant" in t:
        return "quadratic_equation"
    if "shift" in t or "reflection" in t or "stretch" in t or "compress" in t or "transform" in t:
        return rng.choice(["evaluate_function", "polynomial_evaluation"])
    if "factor theorem" in t or "remainder theorem" in t:
        return "polynomial_evaluation"
    if "angle sum" in t or "angle" in t and "identit" in t:
        return "trig_evaluate"
    if "eliminate" in t and "parameter" in t:
        return "solve_linear_equation"
    if "paths and cycle" in t or "connected component" in t or "tree" in t or "graph traversal" in t:
        return "outdegree"
    if "venn" in t or "cartesian product" in t:
        return rng.choice(["set_operation", "combinatorics_basic"])
    if "inverse matri" in t or "identity matri" in t:
        return rng.choice(["determinant_2x2", "matrix_entry"])
    if "consistency" in t or "parametric solution" in t:
        return "system_of_equations"
    if "continuity" in t or "intermediate value" in t:
        return "limit_polynomial"
    if "power rule" in t:
        return "power_rule"
    if "linear system" in t and "ode" in t or "laplace" in t:
        return "eigenvalue_2x2"
    if "equality constraint" in t or "karush" in t or "kkt" in t or "linear programming" in t:
        return "system_of_equations"
    if "prove" in t or "proof" in t:
        return "logic_truth_value"

    # ── Catch-all: fall back gracefully ───────────────────────────────────────
    if "root" in t:
        return "root_concept"
    if "vector" in t:
        return rng.choice(["dot_product", "linear_combination", "vector_norm"])
    if "function" in t:
        return "evaluate_function"
    if "matrix" in t:
        return rng.choice(["matrix_entry", "matrix_vector_product"])

    return None


# ─────────────────────────────────────────────────────────────────────────────
# Regression
# ─────────────────────────────────────────────────────────────────────────────

def generate_linear_regression_fit(rng, difficulty):
    x1 = rng.randint(-3, 1)
    x2 = rng.randint(2, 5)
    m = rng.randint(-3, 4)
    b = rng.randint(-5, 5)
    y1 = m * x1 + b
    y2 = m * x2 + b

    return make_task(
        "Fit a line (least squares)",
        f"({x1},\\ {y1}),\\quad ({x2},\\ {y2})",
        "Find slope m and intercept b of the best-fit line y = mx + b.",
        f"{m},{b}",
        f"{m},{b}|{m} {b}|m={m},b={b}|m={m} b={b}",
        "Use the two points to compute m = (y2−y1)/(x2−x1), then b.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Arithmetic / Algebra
# ─────────────────────────────────────────────────────────────────────────────

def generate_arithmetic(rng, difficulty):
    a = rng.randint(4, 15)
    b = rng.randint(2, 9)
    c = rng.randint(1, 8)
    answer = a - b + c
    return make_task(
        "Arithmetic calculation",
        f"{a}-{b}+{c}",
        "Compute the value.",
        str(answer), str(answer),
        "Work left to right.",
        difficulty,
    )


def generate_fractions(rng, difficulty):
    denominator = rng.choice([6, 8, 9, 10, 12, 15])
    numerator = rng.randint(2, denominator - 1)
    frac = Fraction(numerator, denominator)
    return make_task(
        "Simplify a fraction",
        f"\\frac{{{numerator}}}{{{denominator}}}",
        "Simplify the fraction fully.",
        str(frac), accepted_numeric(frac),
        "Divide numerator and denominator by their GCD.",
        difficulty,
    )


def generate_simplify_expression(rng, difficulty):
    a = rng.randint(2, 6)
    b = rng.randint(2, 6)
    c = rng.randint(1, 4)
    total = a + b - c
    return make_task(
        "Combine like terms",
        f"{a}x+{b}x-{c}x",
        "Simplify the expression.",
        f"{total}x", f"{total}x|{total}*x",
        "Combine all x-coefficients.",
        difficulty,
    )


def generate_simplify_polynomial(rng, difficulty):
    a = rng.randint(2, 5)
    b = rng.randint(2, 5)
    c = rng.randint(1, 4)
    total = a + b
    return make_task(
        "Simplify polynomial",
        f"{a}x^2+{b}x^2-{c}x+{c}x",
        "Simplify the polynomial.",
        f"{total}x^2", f"{total}x^2|{total}*x^2",
        "Combine like-degree terms.",
        difficulty,
    )


def generate_solve_linear_equation(rng, difficulty):
    a = rng.randint(2, 6)
    x = rng.randint(2, 9)
    b = rng.randint(1, 8)
    right = a * x + b
    return make_task(
        "Solve linear equation",
        f"{a}x+{b}={right}",
        "Solve for x.",
        str(x), f"{x}|x={x}|x = {x}",
        f"Subtract {b} from both sides, then divide by {a}.",
        difficulty,
    )


def generate_quadratic_equation(rng, difficulty):
    # Roots r1, r2 chosen so answer is exact integers
    r1 = rng.randint(-5, -1)
    r2 = rng.randint(1, 5)
    # x² - (r1+r2)x + r1*r2 = 0
    b = -(r1 + r2)
    c = r1 * r2
    b_sign = f"+{b}" if b >= 0 else str(b)
    c_sign = f"+{c}" if c >= 0 else str(c)
    r_lo, r_hi = min(r1, r2), max(r1, r2)
    return make_task(
        "Solve quadratic equation",
        f"x^2{b_sign}x{c_sign}=0",
        "Find both roots. Enter as smaller,larger.",
        f"{r_lo},{r_hi}",
        f"{r_lo},{r_hi}|{r_lo} and {r_hi}|x={r_lo} x={r_hi}|{r_lo} {r_hi}",
        f"Use the quadratic formula or factor into (x−{r1})(x−{r2})=0.",
        difficulty,
    )


def generate_factoring_quadratic(rng, difficulty):
    r1 = rng.randint(-4, -1)
    r2 = rng.randint(1, 4)
    b = -(r1 + r2)
    c = r1 * r2
    b_sign = f"+{b}" if b >= 0 else str(b)
    c_sign = f"+{c}" if c >= 0 else str(c)
    p = -r1  # factor: (x + p)
    q = -r2  # factor: (x + q)  … note r2 > 0 so q < 0
    p_sign = f"+{p}" if p >= 0 else str(p)
    q_sign = f"+{q}" if q >= 0 else str(q)
    answer = f"(x{p_sign})(x{q_sign})"
    return make_task(
        "Factor the quadratic",
        f"x^2{b_sign}x{c_sign}",
        "Write in factored form.",
        answer,
        f"{answer}|(x{q_sign})(x{p_sign})",
        f"Find two numbers that multiply to {c} and add to {b}.",
        difficulty,
    )


def generate_system_of_equations(rng, difficulty):
    x = rng.randint(1, 5)
    y = rng.randint(1, 5)
    # Eq1: x + y = s1,  Eq2: x - y = s2
    s1 = x + y
    s2 = x - y
    s2_str = f"+{s2}" if s2 >= 0 else str(s2)
    return make_task(
        "Solve the system",
        f"\\begin{{cases}}x+y={s1}\\\\x-y={s2}\\end{{cases}}",
        "Solve for x and y. Enter as x,y.",
        f"{x},{y}",
        f"{x},{y}|x={x},y={y}|x={x} y={y}|({x},{y})",
        "Add the two equations to eliminate y.",
        difficulty,
    )


def generate_linear_inequality(rng, difficulty):
    a = rng.randint(2, 5)
    b = rng.randint(1, 8)
    c = rng.randint(10, 20)
    # a*x + b < c  →  x < (c-b)/a
    bound = Fraction(c - b, a)
    return make_task(
        "Solve the inequality",
        f"{a}x+{b}<{c}",
        "Solve for x. Enter the boundary value (e.g. 3/2).",
        str(bound),
        accepted_numeric(bound),
        f"Subtract {b}, then divide by {a}.",
        difficulty,
    )


def generate_absolute_value_eq(rng, difficulty):
    a = rng.randint(1, 5)
    b = rng.randint(1, 4)
    # |x - a| = b  →  x = a+b or x = a-b
    x1 = a + b
    x2 = a - b
    lo, hi = min(x1, x2), max(x1, x2)
    return make_task(
        "Solve absolute value equation",
        f"|x-{a}|={b}",
        "Find both solutions. Enter as smaller,larger.",
        f"{lo},{hi}",
        f"{lo},{hi}|{lo} and {hi}|{lo} {hi}",
        "Split into two cases: x−a=b and x−a=−b.",
        difficulty,
    )


def generate_exponent_rules(rng, difficulty):
    base = rng.choice([2, 3, 5])
    p = rng.randint(2, 5)
    q = rng.randint(2, 5)
    total = p + q
    return make_task(
        "Apply exponent rule",
        f"{base}^{p} \\cdot {base}^{q}",
        f"Simplify. Write as {base}^n — what is n?",
        str(total), str(total),
        "When multiplying same-base powers, add exponents.",
        difficulty,
    )


def generate_polynomial_evaluation(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(0, 5)
    c = rng.randint(0, 4)
    x = rng.randint(1, 4)
    answer = a * x * x + b * x + c
    b_str = f"+{b}" if b else ""
    c_str = f"+{c}" if c else ""
    return make_task(
        "Evaluate polynomial",
        f"p(x)={a}x^2{b_str}x{c_str},\\quad p({x})=?",
        "Compute p(x).",
        str(answer), str(answer),
        f"Substitute x={x} and compute each term.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Functions
# ─────────────────────────────────────────────────────────────────────────────

def generate_substitution(rng, difficulty):
    c = rng.randint(2, 9)
    x = rng.randint(2, 5)
    answer = x * x - c
    return make_task(
        "Substitute and evaluate",
        f"x^2-{c},\\quad x={x}",
        f"Substitute x={x} and compute.",
        str(answer), str(answer),
        f"Compute {x}²−{c}.",
        difficulty,
    )


def generate_evaluate_function(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(1, 5)
    x = rng.randint(2, 5)
    answer = a * x * x - b * x
    return make_task(
        "Evaluate function",
        f"f(x)={a}x^2-{b}x,\\quad f({x})=?",
        "Evaluate the function.",
        str(answer), str(answer),
        f"Substitute x={x}.",
        difficulty,
    )


def generate_sign_of_function(rng, difficulty):
    c = rng.choice([5, 10, 17, 26])
    x = int(c ** 0.5)
    answer = x * x - c
    sign = "negative" if answer < 0 else "positive"
    return make_task(
        "Determine sign of function value",
        f"f(x)=x^2-{c},\\quad f({x})=?",
        "Compute the value.",
        str(answer), f"{answer}|{sign}",
        f"Compute {x}²−{c}.",
        difficulty,
    )


def generate_logarithm_basic(rng, difficulty):
    base = rng.choice([2, 3, 5, 10])
    exp = rng.randint(1, 4)
    value = base ** exp
    return make_task(
        "Evaluate logarithm",
        f"\\log_{{{base}}}({value})",
        f"Compute log base {base} of {value}.",
        str(exp), str(exp),
        f"Ask: {base} to what power equals {value}?",
        difficulty,
    )


def generate_exponential_evaluate(rng, difficulty):
    base = rng.choice([2, 3, 4])
    exp = rng.randint(2, 5)
    answer = base ** exp
    return make_task(
        "Evaluate exponential",
        f"{base}^{{{exp}}}",
        "Compute the value.",
        str(answer), str(answer),
        f"Multiply {base} by itself {exp} times.",
        difficulty,
    )


def generate_trig_evaluate(rng, difficulty):
    # Standard angles with exact values
    table = [
        (0,   "\\sin(0°)",           0,    "0"),
        (30,  "\\sin(30°)",    "1/2",  "1/2|0.5"),
        (45,  "\\sin(45°)",  "\\frac{\\sqrt{2}}{2}", "√2/2|0.707"),
        (60,  "\\sin(60°)",  "\\frac{\\sqrt{3}}{2}", "√3/2|0.866"),
        (90,  "\\sin(90°)",           1,    "1"),
        (0,   "\\cos(0°)",            1,    "1"),
        (30,  "\\cos(30°)",  "\\frac{\\sqrt{3}}{2}", "√3/2|0.866"),
        (45,  "\\cos(45°)",  "\\frac{\\sqrt{2}}{2}", "√2/2|0.707"),
        (60,  "\\cos(60°)",   "1/2",  "1/2|0.5"),
        (90,  "\\cos(90°)",           0,    "0"),
    ]
    row = rng.choice(table)
    angle, latex_expr, answer_display, accepted = row
    return make_task(
        "Evaluate trig function",
        latex_expr,
        "Give the exact value.",
        str(answer_display), accepted,
        "Use the unit circle or standard angle table.",
        difficulty,
    )


def generate_inverse_function_value(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(1, 5)
    # f(x) = a*x + b, so f(x0) = y0 where x0 is chosen
    x0 = rng.randint(1, 4)
    y0 = a * x0 + b
    return make_task(
        "Inverse function value",
        f"f(x)={a}x+{b},\\quad f^{{-1}}({y0})=?",
        "Find the inverse function value.",
        str(x0), f"{x0}|x={x0}",
        f"Solve {a}x+{b}={y0} for x.",
        difficulty,
    )


def generate_composite_function(rng, difficulty):
    a = rng.randint(1, 3)
    b = rng.randint(0, 4)
    # f(x) = x^2, g(x) = a*x + b
    # f(g(x)) = (a*x+b)^2 — evaluate at x=1
    x = 1
    inner = a * x + b
    answer = inner * inner
    return make_task(
        "Evaluate composite function",
        f"f(x)=x^2,\\quad g(x)={a}x+{b}",
        "Compute f(g(1)).",
        str(answer), str(answer),
        f"First compute g(1)={a}·1+{b}={inner}, then f({inner}).",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Calculus
# ─────────────────────────────────────────────────────────────────────────────

def generate_power_rule(rng, difficulty):
    n = rng.randint(2, 6)
    coefficient = n
    power = n - 1
    if power == 1:
        answer = f"{coefficient}x"
        accepted = f"{coefficient}x|{coefficient}*x"
    else:
        answer = f"{coefficient}x^{power}"
        accepted = f"{coefficient}x^{power}|{coefficient}*x^{power}"
    return make_task(
        "Differentiate: power rule",
        f"(x^{n})'",
        "Find the derivative.",
        answer, accepted,
        "Use (xⁿ)' = n·xⁿ⁻¹.",
        difficulty,
    )


def generate_polynomial_derivative(rng, difficulty):
    a = rng.randint(2, 6)
    b = rng.randint(1, 5)
    c = rng.randint(1, 5)
    first = 2 * a
    answer = f"{first}x-{b}"
    return make_task(
        "Differentiate polynomial",
        f"f(x)={a}x^2-{b}x+{c}",
        "Find f'(x).",
        answer, f"{answer}|{first}*x-{b}",
        "Differentiate term by term.",
        difficulty,
    )


def generate_evaluate_derivative(rng, difficulty):
    a = rng.randint(2, 6)
    b = rng.randint(1, 5)
    x = rng.randint(2, 5)
    answer = 2 * a * x - b
    return make_task(
        "Evaluate derivative at a point",
        f"f(x)={a}x^2-{b}x,\\quad f'({x})=?",
        "Compute the derivative value.",
        str(answer), str(answer),
        "Find f'(x) first, then substitute.",
        difficulty,
    )


def generate_chain_rule(rng, difficulty):
    n = rng.randint(2, 5)
    a = rng.randint(2, 4)
    # f(x) = (ax)^n  →  f'(x) = n·a·(ax)^(n-1)
    outer = n
    inner_d = a
    coeff = outer * inner_d
    exp = n - 1
    if exp == 1:
        answer = f"{coeff}({a}x)"
        accepted = f"{coeff}({a}x)|{coeff}*({a}x)"
    else:
        answer = f"{coeff}({a}x)^{exp}"
        accepted = f"{coeff}({a}x)^{exp}|{coeff}*({a}x)^{exp}"
    return make_task(
        "Differentiate: chain rule",
        f"f(x)=({a}x)^{n}",
        "Find f'(x) using the chain rule.",
        answer, accepted,
        f"Outer: {n}u^{n-1}, inner derivative: {a}.",
        difficulty,
    )


def generate_product_rule(rng, difficulty):
    # f(x)=x^a, g(x)=x^b  →  (f·g)' = a·x^(a+b-1) + b·x^(a+b-1) = (a+b)·x^(a+b-1)
    a = rng.randint(2, 4)
    b = rng.randint(2, 4)
    # Let's use f(x)=x^a, g(x)=x^b for simplicity
    total_exp = a + b - 1
    coeff = a + b
    answer = f"{coeff}x^{total_exp}"
    return make_task(
        "Differentiate: product rule",
        f"h(x)=x^{a} \\cdot x^{b}",
        "Find h'(x).",
        answer, f"{answer}|{coeff}*x^{total_exp}",
        f"Simplify first: x^{a+b}, then differentiate.",
        difficulty,
    )


def generate_quotient_rule(rng, difficulty):
    # f(x) = (ax + b) / c  →  f'(x) = a/c
    a = rng.randint(2, 6)
    b = rng.randint(1, 5)
    c = rng.randint(2, 5)
    answer = Fraction(a, c)
    return make_task(
        "Differentiate: quotient rule",
        f"f(x)=\\frac{{{a}x+{b}}}{{{c}}}",
        "Find f'(x).",
        str(answer), accepted_numeric(answer),
        "The denominator is constant, so just differentiate the numerator and divide by c.",
        difficulty,
    )


def generate_limit_polynomial(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(1, 5)
    c = rng.randint(0, 4)
    x = rng.randint(1, 4)
    # f(x) = a*x^2 + b*x + c
    answer = a * x * x + b * x + c
    b_str = f"+{b}" if b >= 0 else str(b)
    c_str = f"+{c}" if c >= 0 else str(c)
    return make_task(
        "Evaluate limit",
        f"\\lim_{{x \\to {x}}}\\left({a}x^2{b_str}x{c_str}\\right)",
        "Compute the limit.",
        str(answer), str(answer),
        "For polynomials, just substitute the value.",
        difficulty,
    )


def generate_power_rule_integral(rng, difficulty):
    n = rng.randint(1, 5)
    denom = n + 1
    # ∫ x^n dx = x^(n+1)/(n+1) + C
    if denom == 1:
        answer = "x+C"
        accepted = "x+C|x + C"
    else:
        frac = Fraction(1, denom)
        answer = f"\\frac{{1}}{{{denom}}}x^{{{denom}}}+C"
        accepted = f"1/{denom} x^{denom}+C|x^{denom}/{denom}+C"
    return make_task(
        "Integrate: power rule",
        f"\\int x^{n}\\,dx",
        "Find the antiderivative (include +C).",
        answer, accepted,
        f"Use ∫xⁿ dx = xⁿ⁺¹/(n+1)+C with n={n}.",
        difficulty,
    )


def generate_definite_integral(rng, difficulty):
    # ∫_a^b x dx = b²/2 - a²/2
    a = rng.randint(0, 3)
    b = a + rng.randint(1, 4)
    answer = Fraction(b * b - a * a, 2)
    return make_task(
        "Evaluate definite integral",
        f"\\int_{{{a}}}^{{{b}}} x\\,dx",
        "Compute the definite integral.",
        str(answer), accepted_numeric(answer),
        f"Antiderivative is x²/2. Evaluate at {b} and {a}.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Root finding
# ─────────────────────────────────────────────────────────────────────────────

def generate_root_concept(rng, difficulty):
    root = rng.randint(2, 6)
    c = root * root
    return make_task(
        "Find a root",
        f"x^2-{c}=0",
        "Find the positive root.",
        str(root), str(root),
        f"Solve x²={c}.",
        difficulty,
    )


def generate_check_sign_change(rng, difficulty):
    left = -rng.randint(1, 6)
    right = rng.randint(1, 6)
    return make_task(
        "Check for sign change",
        f"f(a)={left},\\quad f(b)={right}",
        "Do the endpoint signs differ? Answer yes or no.",
        "yes", "yes|true|Yes",
        "One value is negative and the other positive.",
        difficulty,
    )


def generate_midpoint(rng, difficulty):
    a = rng.randint(1, 5)
    b = a + rng.choice([4, 6, 8])
    m = Fraction(a + b, 2)
    return make_task(
        "Find bisection midpoint",
        f"a={a},\\quad b={b}",
        "Compute the midpoint m.",
        str(m), accepted_numeric(m),
        "Use m = (a+b)/2.",
        difficulty,
    )


def generate_interval_update(rng, difficulty):
    a = rng.randint(1, 3)
    m = a + 2
    b = m + 2
    return make_task(
        "Update bisection interval",
        f"f({a})<0,\\quad f({m})>0,\\quad f({b})>0",
        f"After midpoint m={m}, which interval keeps the root?",
        f"[{a},{m}]",
        f"[{a},{m}]|[{a}, {m}]|{a},{m}",
        "Keep the interval where the signs differ.",
        difficulty,
    )


def generate_bisection_step(rng, difficulty):
    a = rng.randint(1, 4)
    b = a + rng.choice([4, 6, 8])
    m = Fraction(a + b, 2)
    return make_task(
        "One bisection step",
        f"[{a},{b}]",
        "Compute the first midpoint.",
        str(m), accepted_numeric(m),
        "Use m = (a+b)/2.",
        difficulty,
    )


def generate_fixed_point_step(rng, difficulty):
    c = rng.choice([5, 10, 17])
    x0 = rng.randint(2, 5)
    answer = Fraction(x0, 1) - Fraction(x0 * x0 - c, 10)
    return make_task(
        "Fixed-point iteration step",
        f"g(x)=x-\\frac{{x^2-{c}}}{{10}},\\quad x_0={x0}",
        "Compute x₁.",
        str(answer), accepted_numeric(answer),
        "Substitute x₀ into g(x).",
        difficulty,
    )


def generate_fixed_point_formula(rng, difficulty):
    c = rng.choice([4, 6, 8, 10])
    denominator = rng.choice([3, 4, 5])
    x0 = rng.randint(1, 4)
    answer = Fraction(x0 + c, denominator)
    return make_task(
        "Apply fixed-point formula",
        f"g(x)=\\frac{{x+{c}}}{{{denominator}}},\\quad x_0={x0}",
        "Compute x₁.",
        str(answer), accepted_numeric(answer),
        "Substitute x₀ into g(x).",
        difficulty,
    )


def generate_contraction_check(rng, difficulty):
    denominator = rng.choice([5, 10])
    x = rng.randint(1, denominator - 1)
    value = abs(1 - Fraction(x, denominator))
    return make_task(
        "Contraction constant",
        f"g'(x)=1-\\frac{{x}}{{{denominator}}},\\quad x={x}",
        f"Compute |g'({x})|.",
        str(value), accepted_numeric(value),
        "Substitute x and take the absolute value.",
        difficulty,
    )


def generate_newton_formula_application(rng, difficulty):
    xk = rng.randint(2, 6)
    fx = rng.randint(2, 8)
    dfx = rng.randint(2, 8)
    answer = Fraction(xk, 1) - Fraction(fx, dfx)
    return make_task(
        "Apply Newton's formula",
        f"x_k={xk},\\quad f(x_k)={fx},\\quad f'(x_k)={dfx}",
        "Compute x_{k+1} = x_k − f(x_k)/f'(x_k).",
        str(answer), accepted_numeric(answer),
        "Substitute values into the formula.",
        difficulty,
    )


def generate_newton_step(rng, difficulty):
    c = rng.choice([5, 10, 17, 26])
    x0 = int(c ** 0.5) + 1
    answer = Fraction(x0, 1) - Fraction(x0 * x0 - c, 2 * x0)
    return make_task(
        "Newton's method: first step",
        f"f(x)=x^2-{c},\\quad x_0={x0}",
        "Compute x₁.",
        str(answer), accepted_numeric(answer),
        "Use x₁ = x₀ − f(x₀)/f'(x₀).",
        difficulty,
    )


def generate_newton_second_step(rng, difficulty):
    c = rng.choice([5, 10])
    x0 = int(c ** 0.5) + 1
    x1 = Fraction(x0, 1) - Fraction(x0 * x0 - c, 2 * x0)
    x2 = Fraction(x1, 1) - Fraction(x1 * x1 - c, 2 * x1)
    return make_task(
        "Newton's method: second step",
        f"f(x)=x^2-{c},\\quad x_1={x1}",
        "Compute x₂.",
        str(x2), accepted_numeric(x2),
        "Apply Newton's formula again with x₁.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Linear Algebra
# ─────────────────────────────────────────────────────────────────────────────

def generate_matrix_entry(rng, difficulty):
    a, b, c, d = [rng.randint(1, 9) for _ in range(4)]
    return make_task(
        "Read matrix entry",
        f"A=\\begin{{pmatrix}}{a}&{b}\\\\{c}&{d}\\end{{pmatrix}}",
        "Compute A₂₁ (row 2, column 1).",
        str(c), str(c),
        "Row index comes first.",
        difficulty,
    )


def generate_matrix_vector_product(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(1, 4)
    c = rng.randint(1, 4)
    d = rng.randint(1, 4)
    first = a + b
    second = c + d
    return make_task(
        "Matrix–vector product",
        f"\\begin{{pmatrix}}{a}&{b}\\\\{c}&{d}\\end{{pmatrix}}\\begin{{pmatrix}}1\\\\1\\end{{pmatrix}}",
        "Compute the product. Enter as r1,r2.",
        f"{first},{second}",
        f"{first},{second}|({first},{second})|[{first},{second}]",
        "Multiply each row by the vector.",
        difficulty,
    )


def generate_matrix_norm(rng, difficulty):
    a = rng.randint(1, 4)
    b = -rng.randint(1, 4)
    c = rng.randint(1, 4)
    d = rng.randint(1, 4)
    norm = max(abs(a) + abs(b), abs(c) + abs(d))
    return make_task(
        "Infinity norm of a matrix",
        f"\\begin{{pmatrix}}{a}&{b}\\\\{c}&{d}\\end{{pmatrix}}",
        "Compute the infinity norm ‖A‖∞.",
        str(norm), str(norm),
        "Take the maximum absolute row sum.",
        difficulty,
    )


def generate_diagonal_dominance(rng, difficulty):
    return make_task(
        "Diagonal dominance check",
        "\\begin{pmatrix}5&1\\\\2&6\\end{pmatrix}",
        "Is the matrix strictly diagonally dominant? Answer yes or no.",
        "yes", "yes|true|Yes",
        "Each diagonal entry must exceed the sum of absolute off-diagonal entries in its row.",
        difficulty,
    )


def generate_determinant_2x2(rng, difficulty):
    a = rng.randint(1, 6)
    b = rng.randint(1, 6)
    c = rng.randint(1, 6)
    d = rng.randint(1, 6)
    det = a * d - b * c
    return make_task(
        "Determinant of 2×2 matrix",
        f"\\det\\begin{{pmatrix}}{a}&{b}\\\\{c}&{d}\\end{{pmatrix}}",
        "Compute the determinant.",
        str(det), str(det),
        "Use ad − bc.",
        difficulty,
    )


def generate_eigenvalue_2x2(rng, difficulty):
    # Diagonal matrix — eigenvalues are just the diagonal entries
    lam1 = rng.randint(1, 5)
    lam2 = rng.randint(1, 5)
    lo, hi = min(lam1, lam2), max(lam1, lam2)
    return make_task(
        "Eigenvalues of a diagonal matrix",
        f"A=\\begin{{pmatrix}}{lo}&0\\\\0&{hi}\\end{{pmatrix}}",
        "List the eigenvalues. Enter as smaller,larger.",
        f"{lo},{hi}",
        f"{lo},{hi}|λ={lo} λ={hi}|{lo} and {hi}",
        "For a diagonal matrix, eigenvalues are the diagonal entries.",
        difficulty,
    )


def generate_dot_product(rng, difficulty):
    a1, a2 = rng.randint(1, 5), rng.randint(1, 5)
    b1, b2 = rng.randint(1, 5), rng.randint(1, 5)
    answer = a1 * b1 + a2 * b2
    return make_task(
        "Compute dot product",
        f"\\mathbf{{u}}=\\begin{{pmatrix}}{a1}\\\\{a2}\\end{{pmatrix}},\\quad"
        f"\\mathbf{{v}}=\\begin{{pmatrix}}{b1}\\\\{b2}\\end{{pmatrix}}",
        "Compute u · v.",
        str(answer), str(answer),
        "Multiply corresponding components and sum.",
        difficulty,
    )


def generate_vector_norm(rng, difficulty):
    # Pick a Pythagorean triple factor so norm is integer
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
    a, b, c = rng.choice(triples)
    return make_task(
        "Compute vector norm",
        f"\\mathbf{{v}}=\\begin{{pmatrix}}{a}\\\\{b}\\end{{pmatrix}}",
        "Compute ‖v‖₂.",
        str(c), str(c),
        f"Use √({a}²+{b}²).",
        difficulty,
    )


def generate_linear_combination(rng, difficulty):
    a = rng.randint(1, 3)
    b = rng.randint(1, 3)
    # vectors (1,0) and (0,1)
    x = a
    y = b
    return make_task(
        "Linear combination of vectors",
        f"{a}\\begin{{pmatrix}}1\\\\0\\end{{pmatrix}}+{b}\\begin{{pmatrix}}0\\\\1\\end{{pmatrix}}",
        "Compute the result. Enter as x,y.",
        f"{x},{y}",
        f"{x},{y}|({x},{y})|[{x},{y}]",
        "Multiply each vector by its scalar, then add.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# PageRank
# ─────────────────────────────────────────────────────────────────────────────

def generate_outdegree(rng, difficulty):
    outdegree = rng.randint(2, 4)
    targets = ",".join(str(i) for i in range(2, outdegree + 2))
    return make_task(
        "Count outdegree",
        f"1\\to {targets}",
        "Compute the outdegree of node 1.",
        str(outdegree), str(outdegree),
        "Count outgoing edges.",
        difficulty,
    )


def generate_distribute_weight(rng, difficulty):
    outdegree = rng.randint(2, 4)
    targets = ",".join(str(i) for i in range(2, outdegree + 2))
    answer = Fraction(1, outdegree)
    return make_task(
        "Distribute PageRank weight",
        f"1\\to {targets}",
        "What weight goes to each outgoing link?",
        str(answer), accepted_numeric(answer),
        "Divide 1 by the outdegree.",
        difficulty,
    )


def generate_transition_entry(rng, difficulty):
    outdegree = rng.randint(2, 4)
    answer = Fraction(1, outdegree)
    return make_task(
        "Transition matrix entry",
        f"1\\to 2,3,\\ldots,{outdegree + 1}",
        "Compute A₂₁ in the transition matrix.",
        str(answer), accepted_numeric(answer),
        "Node 1 distributes weight equally.",
        difficulty,
    )


def generate_column_sum(rng, difficulty):
    return make_task(
        "Column sum of stochastic matrix",
        "A_{\\cdot 1}=\\begin{pmatrix}0\\\\1/2\\\\1/2\\end{pmatrix}",
        "Compute the sum of column 1.",
        "1", "1",
        "Sum all column entries.",
        difficulty,
    )


def generate_power_iteration(rng, difficulty):
    return make_task(
        "Power iteration step",
        "A=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix},\\quad"
        "\\mathbf{x}=\\begin{pmatrix}1\\\\0\\end{pmatrix}",
        "Compute Ax. Enter as r1,r2.",
        "0,1", "[0,1]|(0,1)|0,1",
        "Multiply each row by x.",
        difficulty,
    )


def generate_pagerank_step(rng, difficulty):
    return make_task(
        "PageRank iteration",
        "A=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix},\\quad"
        "\\mathbf{x}^{(0)}=\\begin{pmatrix}1/2\\\\1/2\\end{pmatrix}",
        "Compute x⁽¹⁾ = Ax⁽⁰⁾. Enter as r1,r2.",
        "1/2,1/2",
        "[1/2,1/2]|(1/2,1/2)|0.5,0.5",
        "Multiply A by x⁽⁰⁾.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Interpolation / Splines
# ─────────────────────────────────────────────────────────────────────────────

def generate_polynomial_form(rng, difficulty):
    degree = rng.randint(2, 4)
    answer = degree + 1
    return make_task(
        "Count polynomial coefficients",
        f"p_{{{degree}}}(x)=c_0+c_1x+\\ldots+c_{{{degree}}}x^{{{degree}}}",
        "How many coefficients must be determined?",
        str(answer), str(answer),
        "A degree-n polynomial has n+1 coefficients.",
        difficulty,
    )


def generate_vandermonde_row(rng, difficulty):
    x = rng.randint(2, 5)
    row = [1, x, x * x]
    return make_task(
        "Build Vandermonde row",
        f"p_2(x)=c_0+c_1x+c_2x^2,\\quad x={x}",
        f"Write the Vandermonde row for x={x}. Enter as a,b,c.",
        f"{row[0]},{row[1]},{row[2]}",
        f"[{row[0]},{row[1]},{row[2]}]|({row[0]},{row[1]},{row[2]})|{row[0]},{row[1]},{row[2]}",
        f"Use [1, x, x²] = [1, {x}, {x}²].",
        difficulty,
    )


def generate_lagrange_basis_value(rng, difficulty):
    return make_task(
        "Lagrange basis value at own node",
        "L_i(x_i)",
        "Compute this value.",
        "1", "1",
        "Each Lagrange basis polynomial equals 1 at its own node.",
        difficulty,
    )


def generate_lagrange_term(rng, difficulty):
    coefficient = rng.randint(2, 5)
    return make_task(
        "Compute Lagrange term",
        f"y_i={coefficient},\\quad L_i(x)=x^2",
        "Compute y_i · L_i(x).",
        f"{coefficient}x^2",
        f"{coefficient}x^2|{coefficient}*x^2",
        "Multiply the data value by the basis polynomial.",
        difficulty,
    )


def generate_spline_pieces(rng, difficulty):
    points = rng.randint(3, 6)
    pieces = points - 1
    return make_task(
        "Count spline intervals",
        f"{points}\\text{{ data points}}",
        "How many piecewise intervals are there?",
        str(pieces), str(pieces),
        "The number of intervals is one less than the number of points.",
        difficulty,
    )


def generate_first_derivative_continuity(rng, difficulty):
    value = rng.randint(-5, 5)
    return make_task(
        "First derivative continuity",
        f"S_1'(0)={value},\\quad S_2'(0)=?",
        "Find S₂'(0) for the spline to be smooth.",
        str(value), str(value),
        "Continuity of first derivative requires they match.",
        difficulty,
    )


def generate_second_derivative_continuity(rng, difficulty):
    value = rng.randint(-5, 5)
    return make_task(
        "Second derivative continuity",
        f"S_1''(0)={value},\\quad S_2''(0)=?",
        "Find S₂''(0) for continuity.",
        str(value), str(value),
        "Continuity of second derivative requires they match.",
        difficulty,
    )


def generate_natural_boundary(rng, difficulty):
    return make_task(
        "Natural spline boundary conditions",
        "S''(x_0)=?,\\quad S''(x_n)=?",
        "Give both boundary values for a natural spline. Enter as a,b.",
        "0,0", "0,0|0 and 0",
        "Natural spline: second derivative is zero at both endpoints.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Discrete Mathematics
# ─────────────────────────────────────────────────────────────────────────────

def generate_set_operation(rng, difficulty):
    # A = {1..a_max}, B = {b_min..b_max}, compute |A ∪ B|
    a_max = rng.randint(4, 7)
    b_min = rng.randint(3, a_max)
    b_max = rng.randint(a_max, a_max + 4)
    A = set(range(1, a_max + 1))
    B = set(range(b_min, b_max + 1))
    union = A | B
    inter = A & B
    op = rng.choice(["union", "intersection"])
    if op == "union":
        answer = len(union)
        desc = f"|A \\cup B|"
    else:
        answer = len(inter)
        desc = f"|A \\cap B|"
    return make_task(
        f"Set {op}",
        f"A=\\{{1,\\ldots,{a_max}\\}},\\quad B=\\{{{b_min},\\ldots,{b_max}\\}}",
        f"Compute {desc}.",
        str(answer), str(answer),
        "List the elements of each set and apply the operation.",
        difficulty,
    )


def generate_set_cardinality(rng, difficulty):
    n = rng.randint(3, 8)
    m = rng.randint(2, n)
    # |A| = n, |B| = m, |A ∩ B| = k, compute |A ∪ B| = n + m - k
    k = rng.randint(1, m)
    union_size = n + m - k
    return make_task(
        "Inclusion–exclusion principle",
        f"|A|={n},\\quad |B|={m},\\quad |A\\cap B|={k}",
        "Compute |A ∪ B|.",
        str(union_size), str(union_size),
        "Use |A ∪ B| = |A| + |B| − |A ∩ B|.",
        difficulty,
    )


def generate_logic_truth_value(rng, difficulty):
    p = rng.choice([True, False])
    q = rng.choice([True, False])
    op = rng.choice(["AND", "OR", "implies"])
    if op == "AND":
        result = p and q
        p_str = "T" if p else "F"
        q_str = "T" if q else "F"
        latex = f"p={p_str},\\ q={q_str},\\ p\\land q=?"
        answer = "T" if result else "F"
        hint = "p AND q is true only when both are true."
    elif op == "OR":
        result = p or q
        p_str = "T" if p else "F"
        q_str = "T" if q else "F"
        latex = f"p={p_str},\\ q={q_str},\\ p\\lor q=?"
        answer = "T" if result else "F"
        hint = "p OR q is true when at least one is true."
    else:
        result = (not p) or q
        p_str = "T" if p else "F"
        q_str = "T" if q else "F"
        latex = f"p={p_str},\\ q={q_str},\\ p\\Rightarrow q=?"
        answer = "T" if result else "F"
        hint = "p → q is false only when p is true and q is false."
    return make_task(
        "Evaluate logical expression",
        latex,
        "Compute the truth value. Answer T or F.",
        answer, f"{answer}|{'True' if answer=='T' else 'False'}",
        hint,
        difficulty,
    )


def generate_big_o_comparison(rng, difficulty):
    pairs = [
        ("n", "n^2", "n", "n"),
        ("n^2", "n^3", "n^2", "n^2"),
        ("\\log n", "n", "\\log n", "log n"),
        ("n", "n\\log n", "n", "n"),
        ("n^3", "2^n", "n^3", "n^3"),
        ("n!", "n^n", "n!", "n!"),
    ]
    lo_latex, hi_latex, lo_ans, lo_accepted = rng.choice(pairs)
    return make_task(
        "Compare growth rates",
        f"O({lo_latex})\\text{{ vs }}O({hi_latex})",
        "Which is asymptotically smaller? Enter the smaller one.",
        lo_ans, lo_accepted,
        "Think about which function grows slower as n→∞.",
        difficulty,
    )


def generate_recurrence_step(rng, difficulty):
    # f(n) = f(n-1) + f(n-2), Fibonacci-like
    seeds = [rng.randint(1, 3), rng.randint(1, 3)]
    a, b = seeds
    c = a + b
    return make_task(
        "Compute recurrence step",
        f"f(1)={a},\\quad f(2)={b},\\quad f(n)=f(n-1)+f(n-2)",
        "Compute f(3).",
        str(c), str(c),
        "Substitute n=3: f(3) = f(2) + f(1).",
        difficulty,
    )


def generate_combinatorics_basic(rng, difficulty):
    # Compute C(n, 2) = n*(n-1)/2
    n = rng.randint(4, 8)
    answer = n * (n - 1) // 2
    return make_task(
        "Binomial coefficient",
        f"\\binom{{{n}}}{{2}}",
        "Compute the binomial coefficient.",
        str(answer), str(answer),
        f"Use n(n−1)/2 = {n}·{n-1}/2.",
        difficulty,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Additional generators for broader skill coverage
# ─────────────────────────────────────────────────────────────────────────────

def generate_slope_from_points(rng, difficulty):
    x1 = rng.randint(-4, 2)
    x2 = x1 + rng.randint(1, 5)
    m = rng.randint(-3, 4)
    y1 = rng.randint(-5, 5)
    y2 = y1 + m * (x2 - x1)
    answer = Fraction(y2 - y1, x2 - x1)
    return make_task(
        "Compute slope",
        f"({x1},\\ {y1}),\\quad ({x2},\\ {y2})",
        "Compute the slope of the line through these two points.",
        str(answer), accepted_numeric(answer),
        "Use m = (y₂−y₁)/(x₂−x₁).",
        difficulty,
    )


def generate_foil_binomials(rng, difficulty):
    a = rng.randint(1, 4)
    b = rng.randint(1, 4)
    c = rng.randint(1, 4)
    d = rng.randint(1, 4)
    # (ax + b)(cx + d) = acx^2 + (ad+bc)x + bd
    A = a * c
    B = a * d + b * c
    C = b * d
    b_str = f"+{B}" if B >= 0 else str(B)
    c_str = f"+{C}" if C >= 0 else str(C)
    answer = f"{A}x^2{b_str}x{c_str}"
    return make_task(
        "Multiply binomials (FOIL)",
        f"({a}x+{b})({c}x+{d})",
        "Expand the product.",
        answer, f"{answer}|{A}x^2+{B}x+{C}",
        "Use FOIL: First, Outer, Inner, Last.",
        difficulty,
    )


def generate_distributive_property(rng, difficulty):
    a = rng.randint(2, 6)
    b = rng.randint(1, 8)
    c = rng.randint(1, 8)
    ab = a * b
    ac = a * c
    c_str = f"+{ac}" if ac >= 0 else str(ac)
    answer = f"{ab}x{c_str}"
    return make_task(
        "Apply distributive property",
        f"{a}(x+{c})" if c == rng.randint(c, c) else f"{a}({b}x+{c})",
        "Expand the expression.",
        f"{a}x+{a*c}", f"{a}x+{a*c}|{a}*x+{a*c}",
        f"Multiply {a} by each term inside the parentheses.",
        difficulty,
    )


def generate_percent_problem(rng, difficulty):
    percent = rng.choice([10, 20, 25, 50, 75])
    whole = rng.randint(2, 10) * 100 // percent * percent
    answer = whole * percent // 100
    return make_task(
        "Solve percent problem",
        f"{percent}\\%\\text{{ of }}{whole}",
        "Compute the value.",
        str(answer), str(answer),
        f"Multiply {whole} × {percent}/100.",
        difficulty,
    )


def generate_arithmetic_sequence(rng, difficulty):
    a1 = rng.randint(1, 10)
    d = rng.randint(1, 5)
    n = rng.randint(5, 10)
    an = a1 + (n - 1) * d
    return make_task(
        "Arithmetic sequence: nth term",
        f"a_1={a1},\\quad d={d},\\quad n={n}",
        "Find the nth term aₙ.",
        str(an), str(an),
        "Use aₙ = a₁ + (n−1)d.",
        difficulty,
    )


def generate_geometric_sequence(rng, difficulty):
    a1 = rng.randint(1, 4)
    r = rng.randint(2, 3)
    n = rng.randint(3, 6)
    an = a1 * r ** (n - 1)
    return make_task(
        "Geometric sequence: nth term",
        f"a_1={a1},\\quad r={r},\\quad n={n}",
        "Find the nth term aₙ.",
        str(an), str(an),
        "Use aₙ = a₁ · rⁿ⁻¹.",
        difficulty,
    )


def generate_complex_arithmetic(rng, difficulty):
    a = rng.randint(1, 5)
    b = rng.randint(1, 4)
    c = rng.randint(1, 5)
    d = rng.randint(1, 4)
    op = rng.choice(["add", "multiply"])
    if op == "add":
        re = a + c
        im = b + d
        im_str = f"+{im}" if im >= 0 else str(im)
        answer = f"{re}{im_str}i"
        return make_task(
            "Add complex numbers",
            f"({a}+{b}i)+({c}+{d}i)",
            "Compute the sum.",
            answer, f"{answer}|{re}+{im}i",
            "Add real parts and imaginary parts separately.",
            difficulty,
        )
    else:
        # (a+bi)(c+di) = ac-bd + (ad+bc)i
        re = a * c - b * d
        im = a * d + b * c
        im_str = f"+{im}" if im >= 0 else str(im)
        answer = f"{re}{im_str}i"
        return make_task(
            "Multiply complex numbers",
            f"({a}+{b}i)({c}+{d}i)",
            "Compute the product.",
            answer, f"{answer}|{re}+{im}i",
            "Use FOIL and replace i²=−1.",
            difficulty,
        )

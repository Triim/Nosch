import os
import streamlit.components.v1 as components

_COMPONENT = components.declare_component(
    "cytoscape_graph",
    path=os.path.abspath(os.path.join(os.path.dirname(__file__), "frontend")),
)


def render_cytoscape_graph(nodes, edges, height=720, focus_node_id=None, focus_zoom=1.1, key=None):
    return _COMPONENT(
        nodes=nodes,
        edges=edges,
        height=height,
        focusNodeId=focus_node_id,
        focusZoom=focus_zoom,
        key=key,
        default=None,
    )

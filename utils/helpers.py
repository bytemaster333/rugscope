import plotly.graph_objects as go
import streamlit as st

def display_sankey_diagram(edges):
    try:
        from_nodes = [edge["from"] for edge in edges if "from" in edge and "to" in edge and "value" in edge]
        to_nodes = [edge["to"] for edge in edges if "from" in edge and "to" in edge and "value" in edge]
        values = [edge["value"] for edge in edges if "from" in edge and "to" in edge and "value" in edge]

        all_nodes = list(set(from_nodes + to_nodes))
        label_map = {addr: i for i, addr in enumerate(all_nodes)}

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                label=all_nodes,
                line=dict(color="black", width=0.5)
            ),
            link=dict(
                source=[label_map[frm] for frm in from_nodes],
                target=[label_map[to] for to in to_nodes],
                value=values
            )
        )])

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Failed to render Sankey diagram: {e}")

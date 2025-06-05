import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import io

st.title("Graphing Calculator")

# Setup of graph
equation = st.text_input(label="Equation (in terms of x):", value="sin(x)")
x_lower_boundary = st.text_input(label="X Lower Boundary", value="0")
x_upper_boundary = st.text_input(label="X Upper Boundary", value="10")
y_lower_boundary = st.text_input(label="Y Lower Boundary (optional)", value="")
y_upper_boundary = st.text_input(label="Y Upper Boundary (optional)", value="")
graph_title = st.text_input(label="Graph Title", value="Graph of equation")
x_label = st.text_input(label="X Axis Label", value="x")
y_label = st.text_input(label="Y Axis Label", value="y")

if equation and x_lower_boundary and x_upper_boundary:
    try:
        # Setting up boundaries
        x_lower = float(x_lower_boundary)
        x_upper = float(x_upper_boundary)
        if y_lower_boundary != "":
            y_lower = float(y_lower_boundary)
        else:
            y_lower = None
        if y_upper_boundary != "":
            y_upper = float(y_upper_boundary)
        else:
            y_upper = None

        # Using sympy to read the equation
        x = sp.symbols('x')
        expression = sp.sympify(equation)
        f = sp.lambdify(x, expression, modules=["numpy"])

        # Graphing part
        num_points = int((x_upper - x_lower) * 10)
        x_values = np.linspace(x_lower, x_upper, num_points)
        y_values = f(x_values)

        # Plotting the graph
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, label=equation)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(graph_title)
        ax.grid(True)
        ax.legend(equation)

        if y_lower is not None and y_upper is not None:
            ax.set_ylim([y_lower, y_upper])

        st.pyplot(fig)

        # Prepare buffer and download button
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)

        st.download_button(
            label="📥 Download Graph as PNG",
            data=buf,
            file_name=f"{graph_title}.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter the equation and x-axis boundaries to plot the graph.")
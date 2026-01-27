import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

from algorithm import fill_seats
seat_matrix = pd.read_csv("seat_matrix.csv", header=None)

# Set page configuration
st.set_page_config(page_title="LAD Inventory Section", layout="wide")

# Main title and logo
st.title("LAD Inventory Section Dashboard")


col1, col2 = st.columns([1, 2])
with col1:
    pod_size = st.number_input("Pod Size", min_value=1, max_value=18, value=2, step=1, key="pod_size")
    seat_gap = st.number_input("Seat Gap", min_value=1, max_value=5, value=2, step=1, key="seat_gap")
    row_gap = st.number_input("Row Gap", min_value=0, max_value=5, value=1, step=1, key="row_gap")

    filled_matrix, filled_seats = fill_seats(seat_matrix.values.copy(), pod_size, seat_gap, row_gap)
    st.markdown(f"### Total Filled Seats: {filled_seats}")

with col2:
    filled_matrix, filled_seats = fill_seats(seat_matrix.values.copy(), pod_size, seat_gap, row_gap)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')

    sns.heatmap(
        filled_matrix, 
        cmap=["#dfdddd", "#0068c9"],
        cbar=False, 
        linewidths=0.5, 
        linecolor='#262730',
        ax=ax,
        square=True
    )

    ax.set_xlabel('Seat Number')
    ax.set_ylabel('Row')
    ax.set_yticklabels([chr(i) for i in range(65, 65 + filled_matrix.shape[0])], rotation=0, color="#FFFFFF", fontsize=9)
    ax.set_xticklabels(range(1, filled_matrix.shape[1] + 1), rotation=0, color="#FFFFFF", fontsize=9)
    ax.tick_params(colors="#FFFFFF", labelsize=9, length=0)

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


# Assumptions
### Pods cannot go over 18 because that's the max row size
### SeatGap are at least 1 because we need socially distanced seats
### We can fill seats with one row and then nothing in front since social distancing is only horizontal and vertical
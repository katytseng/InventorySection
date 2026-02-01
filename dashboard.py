import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

from algorithm import fill_seats
from algorithm import fill_seats1
seat_matrix = pd.read_csv("seat_matrix.csv", header=None)

st.set_page_config(page_title="LAD Inventory Section", layout="wide")
st.title("LAD Inventory Section Dashboard")


col1, col2 = st.columns([1, 2])
with col1:
    pod_size = st.number_input("Pod Size", min_value=1, max_value=18, value=2, step=1, key="pod_size")
    seat_gap = st.number_input("Seat Gap", min_value=1, max_value=5, value=2, step=1, key="seat_gap")
    row_gap = st.number_input("Row Gap", min_value=0, max_value=5, value=1, step=1, key="row_gap")
    
    filled_seat_img = Image.new('RGB', (20, 20), color='#0068c9')
    empty_seat_img = Image.new('RGB', (15, 15), color='#dfdddd')
    seat_legend_col1, seat_legend_col2 = st.columns([1, 3])
    with seat_legend_col1: st.image(filled_seat_img, caption='Filled Seat')
    with seat_legend_col2:st.image(empty_seat_img, caption='Empty Seat')

    filled_matrix, filled_seats = fill_seats(seat_matrix.values.copy(), pod_size, seat_gap, row_gap)
    filled_matrix1, filled_seats1 = fill_seats1(seat_matrix.values.copy(), pod_size, seat_gap, row_gap)
    st.markdown("### Solutions Comparison")
    summary_df = pd.DataFrame({
        "Solution": ["1", "2"],
        "Filled Seats": [filled_seats, filled_seats1],
        "Percentage Filled": [f"{(filled_seats / 263) * 100:.2f}%", f"{(filled_seats1 / 263) * 100:.2f}%"],
        "Number of Pods": [filled_seats // pod_size, filled_seats1 // pod_size],
        "Empty Seats": [263 - filled_seats, 263 - filled_seats1]
    })
    st.table(summary_df)

    

with col2:
    tab1, tab2 = st.tabs(["Solution 1", "Solution 2"])
    with tab1:
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

        ax.set_xlabel('Seat Number', color="#FFFFFF", fontsize=9)
        ax.set_ylabel('Row', color="#FFFFFF", fontsize=9)
        ax.set_yticklabels([chr(i) for i in range(65, 65 + filled_matrix.shape[0])], rotation=0, color="#FFFFFF", fontsize=9)
        ax.set_xticklabels(range(1, filled_matrix.shape[1] + 1), rotation=0, color="#FFFFFF", fontsize=9)
        ax.tick_params(colors="#FFFFFF", labelsize=9, length=0)

        for spine in ax.spines.values():
            spine.set_visible(False)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    with tab2:
        filled_matrix, filled_seats = fill_seats1(seat_matrix.values.copy(), pod_size, seat_gap, row_gap)

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

        ax.set_xlabel('Seat Number', color="#FFFFFF", fontsize=9)
        ax.set_ylabel('Row', color="#FFFFFF", fontsize=9)
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
import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("best.csv")

# Set Streamlit page configuration
st.set_page_config(page_title="SMART-Fit", layout="centered")

# --- Custom CSS for background image ---
st.markdown("""
    <style>
        body {
            background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20240329/pngtree-rows-of-dumbbells-in-the-gym-image_15662386.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.75); /* white transparent overlay */
            padding: 2rem;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Page header
st.title("🏋️ SMART-Fit")
st.markdown("### Train Smarter – Save Time!")

st.markdown("---")

# Input form container
st.subheader("🔍 Fill in your details to get a personalized workout")
col1, col2 = st.columns(2)

with col1:
    age_group = st.selectbox("Age Group", [""] + sorted(df["Age_Group"].dropna().unique().tolist()))

with col2:
    gender = st.selectbox("Gender", [""] + sorted(df["Gender"].dropna().unique().tolist()))

col3, col4 = st.columns(2)
with col3:
    bmi_cat = st.selectbox("BMI Category", [""] + sorted(df["BMI_Category"].dropna().unique().tolist()))

with col4:
    experience = st.selectbox("Experience Level", [""] + sorted(df["Experience_Level"].dropna().unique().tolist()))

# Show output only when all inputs are selected
if all([age_group, gender, bmi_cat, experience]):
    st.markdown("---")
    st.subheader("🎯 Your Personalized Workout Recommendation")

    # Filter the DataFrame
    filtered_df = df[
        (df["Age_Group"] == age_group) &
        (df["Gender"] == gender) &
        (df["BMI_Category"] == bmi_cat) &
        (df["Experience_Level"] == experience)
    ]

    if not filtered_df.empty:
        recommended = filtered_df["Workout_Type"].value_counts().idxmax()

        # Styled recommendation output
        st.markdown(f"""
        <div style='
            background-color: #e6f7f5; 
            padding: 30px; 
            border-radius: 12px; 
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        '>
            <h2 style='color:#006666;'>🏆 Recommended Workout</h2>
            <h1 style='color:#222;'>{recommended}</h1>
            <p style='font-size: 16px;'>This workout is most suitable based on your profile and previous data.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ No matching data found. Try adjusting your inputs.")
else:
    st.warning("⚠️ Please complete all inputs above to get your workout recommendation.")

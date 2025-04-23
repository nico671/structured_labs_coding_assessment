import pandas as pd  # noqa: F401
import plotly.express as px  # noqa: F401
from preswald import connect, get_df, plotly, table, text

text("# Introduction")
text("Hi! My name is Nicolas Carbone. Thank you for considering my application!")

text(
    "As a current student at the University of Maryland, I thought it was only fitting that I take a look at a dataset of synthetic students"
)
# Load the CSV
connect()
df = get_df("student_habits_performance")


text("# Data Overview")
text("Here is a preview of the dataset:")
# num_rows_to_display = slider(
#     label="Select the number of rows to display",
#     min_val=1,
#     max_val=50,
#     default=10,
# )
# print(f"{num_rows_to_display} rows")
# table(df.head(num_rows_to_display))
# i tried to allow for dynamically updating the amount of rows but i got an error everytime (even the example from the documentation threw an error)
# ERROR: 2025-04-23 13:20:24,902 - preswald.engine.utils - ERROR - Error encoding object <class 'bytes'>: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
table(df.head(10))
text(
    f"The dataset contains {len(df)} rows (students) and {len(df.columns)} columns (features)."
)
text("Columns: " + ", ".join(df.columns))

# text("## Null Values and Data Types")
# col_choice = selectbox(
#     label="Select a column to see its data type and number of null values.",
#     options=list(df.columns),
# )
# text(
#     f"{col_choice}: {df[col_choice].dtype}, {df[col_choice].isnull().sum()} null values"
# )
# this code also caused my code to throw an error everytime, again even the example from the documentation didn't work
text("# Analysis")


def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


df["letter_grade"] = df["exam_score"].apply(assign_letter_grade)
# Demographic Analysis
text("## Demographic Analysis")
text("### Age Distribution")
age_fig = px.histogram(df, x="age", nbins=10, title="Age Distribution")
plotly(age_fig)
text("As expected, the age distribution is fairly uniform across the dataset.")
text(
    "All ages are between 17 and 24 which is about what we expect for college students."
)
text("### Gender Breakdown")
gender_counts = df["gender"].value_counts().reset_index()
gender_counts.columns = ["Gender", "Count"]
gender_fig = px.pie(
    gender_counts, names="Gender", values="Count", title="Gender Breakdown"
)
plotly(gender_fig)
text("The gender breakdown is approximately 50/50, which is great to see.")
# Academic Performance
text("## Academic Performance")
text("### Exam Score Distribution")
score_fig = px.histogram(df, x="exam_score", nbins=20, title="Exam Score Distribution")
plotly(score_fig)
text("We see that exam scores roughly follow a normal distribution, as expected.")

text("### Study Hours vs Exam Scores")
study_fig = px.scatter(
    df,
    x="study_hours_per_day",
    y="exam_score",
    color="letter_grade",
    title="Study Hours vs Exam Scores",
    labels={"study_hours_per_day": "Study Hours Per Day", "exam_score": "Exam Score"},
)
plotly(study_fig)
text(
    "As expected, there is a positive correlation between study hours and exam scores. Proof that no amount of convincing yourself that \"it's just common sense I'll figure it out \" will help you pass an exam."
)
# Lifestyle Factors
text("## Lifestyle Factors")
text("### Social Media Hours vs Exam Scores")
social_fig = px.scatter(
    df,
    x="social_media_hours",
    y="exam_score",
    color="letter_grade",
    title="Social Media Hours vs Exam Scores",
    labels={"social_media_hours": "Social Media Hours", "exam_score": "Exam Score"},
)
plotly(social_fig)
text(
    "Contrary to what my parents are constantly telling me, there doesn't seem to be too strong of a correlation between social media hours and exam scores. I guess I can keep scrolling TikTok for a few more hours."
)
text("### Sleep Hours vs Exam Scores")
sleep_fig = px.scatter(
    df,
    x="sleep_hours",
    y="exam_score",
    color="letter_grade",
    title="Sleep Hours vs Exam Scores",
    labels={"sleep_hours": "Sleep Hours", "exam_score": "Exam Score"},
)
plotly(sleep_fig)
text(
    "There is little to no correlation between sleep hours and exam scores. Across all the letter grades there is an even mix of those who prioritize sleep, and those who cram all night."
)

# # # # Interactive Dashboard
# text("## Interactive Dashboard")
# text("Explore the dataset interactively using the controls below.")

# # Slider for rows to display
# rows_to_display = slider(
#     "Number of Rows to Display", min_val=5, max_val=50, default=10, step=5
# )

# # Column selector
# all_columns = df.columns.tolist()
# selected_columns = selectbox(
#     label="Select Columns to Display",
#     options=all_columns,
#     default="exam_score",
# )

# # Gender filter
# gender_options = ["All"] + df["gender"].unique().tolist()
# selected_gender = selectbox(
#     label="Filter by Gender", options=gender_options, default="All"
# )


# # Apply filters and display table
# def update_table(
#     rows=rows_to_display, columns=selected_columns, gender=selected_gender
# ):
#     filtered_df = df.copy()
#     if gender != "All":
#         filtered_df = filtered_df[filtered_df["gender"] == gender]
#     text(
#         f"Displaying {min(rows, len(filtered_df))} of {len(filtered_df)} matching records."
#     )
#     return table(filtered_df[columns].head(rows))


# update_table(rows=rows_to_display, columns=selected_columns, gender=selected_gender)

# also tried to implement this but for some reason it wouldn't preview when this code was active
# ERROR: 2025-04-23 13:22:23,112 - preswald.engine.utils - ERROR - Error encoding object <class 'bytes'>: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
# ERROR: 2025-04-23 13:22:27,278 - preswald.engine.base_service - ERROR - Error handling message from w04n2z: name 'HASH_PATTERN' is not defined
# Correlation Analysis
text("## Correlation Analysis")
corr_cols = [
    "study_hours_per_day",
    "social_media_hours",
    "sleep_hours",
    "exam_score",
    "netflix_hours",
    "attendance_percentage",
    "mental_health_rating",
    "exercise_frequency",
]
corr_matrix = df[corr_cols].corr()

text("### Correlation Heatmap")
heatmap_fig = px.imshow(
    corr_matrix,
    x=corr_cols,
    y=corr_cols,
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap",
)
plotly(heatmap_fig)
text("This correlation heatmap shows the relationships between various features.")
text("The strongest correlation is between study hours and exam scores, as expected.")
text(
    "There is a slight negative correlation between social media hours / netflix hours and exam scores, but the single most important factor is how long a student studies for!"
)
text("Thank you for reviewing my analysis!")

import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Project Planning", Start = "2025-01-01", Finish = "2025-02-28"),
    dict(Task="Develop Website", Start = "2025-03-01", Finish = "2025-05-15"),
    dict(Task="Review Code", Start = "2025-05-16", Finish = "2025-07-31"),
    dict(Task="Release Product", Start = "2025-08-01", Finish = "2025-09-15")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
fig.update_yaxes(autorange="reversed")
fig.show()

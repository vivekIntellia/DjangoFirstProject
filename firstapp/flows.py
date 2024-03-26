
from viewflow import flow
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView
from .models import Education
from .forms import ReviewEducationForm  # Import the form needed for the flow
from .views import MakeDecisionView  # Import the view needed for the flow

class EducationFlow(Flow):
    process_class = Education

    start = flow.Start(
        CreateProcessView,
        fields=[
            "class_10_school_name", "class_10_board_or_university", "class_10_year_of_passing", "class_10_grade_or_cgpa",
            "class_10_marksheet", "class_10_percentage",
            "class_12_school_name", "class_12_board_or_university", "class_12_year_of_passing", "class_12_grade_or_cgpa",
            "class_12_marksheet", "class_12_percentage",
            "graduation_college_name", "graduation_board_or_university", "graduation_year_of_passing", "graduation_grade_or_cgpa",
            "graduation_marksheet", "graduation_percentage"
        ]
    ).Permission(auto_create=True).Next(this.admin_review)

    admin_review = flow.View(
        ReviewEducationForm,
        fields=[
            "class_10_school_name", "class_10_board_or_university", "class_10_year_of_passing", "class_10_grade_or_cgpa",
            "class_12_school_name", "class_12_board_or_university", "class_12_year_of_passing", "class_12_grade_or_cgpa",
            "graduation_college_name", "graduation_board_or_university", "graduation_year_of_passing", "graduation_grade_or_cgpa",
        ]
    ).Permission(auto_create=True).Next(this.make_decision)

    make_decision = flow.View(
        MakeDecisionView
    ).Permission(auto_create=True).Next(this.decision)

    decision = flow.End()

    end = flow.End()











# flows.py defines the structure and logic of the workflow for handling educational information in the application using the viewflow library.
    # In simple terms, setting process_class = Education helps the workflow understand that it's dealing with Education records, making it easier to manage and work with them within the workflow itself.
    # n summary, this line of code ensures that the necessary permissions are in place for users to access the view, and after completion, it specifies the next step in the workflow.











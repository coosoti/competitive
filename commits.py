import gspread
from oauth2client.service_account import ServiceAccountCredentials
from github import Github
from datetime import datetime, timedelta

# Set up Google Sheets API authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('token.json', scope)
client = gspread.authorize(creds)

# Open the spreadsheet
spreadsheet_key = '15KT3lEamBM44KGRoDgm4Djw0snGqA4YoKedFH-C3_Uk'
sheet = client.open_by_key(spreadsheet_key).sheet1

# Connect to GitHub
github = Github("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")

# Get today's date
today = datetime.utcnow().strftime('%Y-%m-%d')

# Find the next empty column index
next_empty_column = len(sheet.row_values(1)) + 1

# Update the first row with the current date
sheet.update_cell(1, next_empty_column, today)

# Get the list of students from the spreadsheet
students = sheet.get_all_records()

# Iterate through each student
for student in students:
    student_name = student['student_name']
    github_username = student['github_username']
    github_repo = student['github_repo']
    commits_count = 0
    
    # Fetch commits from the student's GitHub repository
    repo = github.get_user(github_username).get_repo(github_repo)
    commits = repo.get_commits(since=datetime.now() - timedelta(days=1))
    
    # Count the number of commits
    commits_count = sum(1 for commit in commits)
    
    # Update the cell with the commit count for the student under today's date
    cell = sheet.find(student_name)  # Find the cell corresponding to the student's name
    sheet.update_cell(cell.row, next_empty_column, commits_count)  # Update the cell with the commit count

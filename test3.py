from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth

def count_important_emails():
    """Count all important emails in the Gmail account."""
    # Set the user you want to impersonate (the user whose emails you want to count)
    user_to_impersonate = "eswarssethu2002@gmail.com"  # Replace with the email of the user to impersonate

    # Load credentials and create the service
    creds, _ = google.auth.default()
    creds = creds.with_subject(user_to_impersonate)

    try:
        service = build("gmail", "v1", credentials=creds)

        # List messages marked as important
        query = "is:important"
        response = service.users().messages().list(userId="me", q=query).execute()
        messages = response.get('messages', [])

        # Count messages
        important_count = len(messages)

        # Handle pagination if there are more than 100 messages
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId="me", q=query, pageToken=page_token).execute()
            messages.extend(response.get('messages', []))
            important_count += len(messages)

        print(f'Total important emails: {important_count}')

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    count_important_emails()

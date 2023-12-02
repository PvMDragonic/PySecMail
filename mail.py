from time import sleep
import requests

class Mail():
    """
    Represents an individual email recieved by Service.
    """

    class Attachment():
        def __init__(self, file: dict) -> None:
            self.filename = file['filename']
            self.type = file['contentType']
            self.size = file['size']

    def __init__(self, res: dict) -> None:
        self.id = res['id']
        self.sender = res['from']
        self.subject = res['subject']
        self.date = res['date']
        self.attachment = Mail.Attachment(res['attachments'])
        self.body = res['body']
        self.textBody = res['textBody']
        self.htmlBody = res['htmlBody']

class Service():
    """
    Manages a temporary email from 1secmail.
    """

    def __init__(self) -> None:
        self.login, self.domain = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()[0].split("@")
        self.mail = f'https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}'

    def address(self) -> str:
        """
        Gets the temporary email's address.
        
        Returns:
            example@something.com
        """
        return f'{self.login}@{self.domain}'
    
    def download(self, mail: Mail) -> bool:
        """
        Downloads a file attached to an email.

        Returns:
            True or False as to the success of the download.
        """

        url = f'https://www.1secmail.com/api/v1/?action=download&login={self.login}&domain={self.domain}.com&id={mail.id}&file={mail.attachment.filename}'
        response = requests.get(url)

        if response.status_code == 200:
            with open(self.filename, 'wb') as file:
                file.write(response.content)

    def inbox(self) -> list[Mail] | None:
        """
        Gets all emails currently on the inbox.

        Returns:
            List of mail objects.
        """

        request = requests.get(self.mail).json()

        if len(request) == 0:
            return None
        
        inbox_ids = [item['id'] for item in request if 'id' in item]

        mails = []
        for id in inbox_ids:
            message = f'https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={id}'
            req = requests.get(message).json()
            mails.append(Mail(req))

        return mails

    def check_for_new(self) -> Mail:
        """
        Blocking operation that looks for a new mail until it finds it.

        Returns:
            Mail object of the most recent inbox entry. 
        """

        curr_amount = len(request = requests.get(self.mail).json())

        while True:
            request = requests.get(self.mail).json()

            if len(request) == curr_amount:
                sleep(5)
                continue
                
            last_id = [item['id'] for item in request if 'id' in item][-1]

            message = f'https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={last_id}'
            req = requests.get(message).json()
            return Mail(req)
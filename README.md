<h1 align="center">PySecMail</h1>
<p align="center">A basic wrapper for the 1secmail API.</p>

## Functionality

### Service class
Responsible for managing the inbox. Generates a random email for every class instance.

#### Attributes
| Name | Description |
| -------- | -------- |
| login | 1secmail's randomly generated email name. |
| domain | 1secmail's randomly generated domain. |
| mail  | Random email getMessages API url.  |

#### Methods
| Name | Description |
| -------- | -------- |
| address | Returns the random email full address. |
| download | Downloads a file from a given email. |
| inbox  | Gets all emails currently in the inbox.  |
| check_for_new | Waits until a new mail comes in and returns it. |

### Mail class
Represents an email recieved by a Service class.

#### Attributes
| Name | Description |
| -------- | -------- |
| id | The email id. |
| sender | The sender's email. |
| subject  | The email subject.  |
| date | The date on which it was recieved. |
| attachment  | An Attachment object.  |
| body | The body of the email. |
| textBody  | The text body of the email.  |
| htmlBody | The html body of the email. |

#### Attachment
Represents a file attachment that a Mail might have.

| Name | Description |
| -------- | -------- |
| filename | The name (with file extension) of the attached file. |
| type | The type of the attached file. |
| size | The size of the attached file.  |
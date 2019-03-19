# Automated-Receipting-System-SIH2019
Automatic Finance Receipting using Robotic Process Automation(RPA)

An automated finance receipting system where transaction invoices are processed automatically and from which data is retrieved. Extracted user information like UserID, Transaction type, amount, payment mode, etc. is fed to the web application. Based on transaction type, client details are segregated as either Card or Cheque. For each Invoice number, templates are used to generate receipts and the same is mailed to the vendor specified in the database. Our solution will automate the above process and email the receipts to corresponding vendor by :
Processing receipts which are uploaded onto the website in the form of a pdf, jpg, png or a zip file.
Picking up files from a particular local path on your computer, which can be triggered by refreshing the website or by any OS event if required. 
It also will flag receipts with incomplete data and log the data into the database and display it on the website. We will also display all the sales statistics on the dashboard including graphs about transaction type, predictions about sales, etc. 

Automate receipting process - Which involves processing and mailing of 25,000 receipts per month will be much faster.
Invoices can be in the form of pdf documents, scanned pdfs or images.
Segregate vendors on the basis of transaction - Card or Cheque.
Generate receipt and send an email for the given vendor transaction.
Optical Character Recognition(OCR) to extract Receipt Data from images.
TIKA library for extracting data from pdfs..
Natural Language Processing (NLP) for structuring extracted data which is uploaded to our database.
It is a client Independent Product and can be easily customized specific to a user according to his requirements.

Dependencies: -

openCV
tika
wkhtmltopdf
zipfile
PIL
pdfkit

Additional features: -

File Handling:
Files from a particular location in the system are loaded continuously. Depending on the type of the file, .jpg, .jpeg, .png and .pdf files are operated on by appropriate functions. Contents on .zip file are extracted. Once the entire processing is done, the file is deleted from the location. The system is continuously checking the source location for any unprocessed files.

Better Speed through Pipelining:
Since we are using the tika server to process pdf files, it uses pipelining to execute with a higher speed of processing 1 file per 1.3 s when we tested on a zip having 100 files.

Autocorrect for customer ID:
In case the OCR mechanism reads an incorrect customer ID that is not present in the database, the system will check for the next ID that is closest to the read one. If the difference between the two IDs is above a defined threshold, the system will automatically correct the misread ID. To ensure safety, the customer IDs will be allotted using the principles of Hamming code, which will avoid any possible clashes

Natural language processing : 
The content from the scanned text from PDF or Image source file needs to be filtered and only the useful required information is to be extracted. The system utilises Python in-built  NLTK library for implementing the same. Having assumed a standard format of invoices, the system identifies fields of interest from the text using the concept of "terms of interest". For every field, there are a list of words that are often used to to depict the field, for eg Total Bill is also termed as Grand Total or Total Amount  in some cases. In this case, the terms of interest for Amount are "Grand", "Total" and "Bill". For most fields the text is parsed line by line. When a line contains one or more terms of interest for a particular field, that line is scanned using Python regular expression engine to extract the useful data in that line. The method of payment is done by scanning the description in invoice and the date is extracted based on various  regular expressions.

OCR using Tesseract :
For extracting text from .jpg, .jpeg and .png files Tesseract is used. First the image is loaded using openCV and it is then preprocessed. For preprocessing, the image is converted to gray-scale and then adaptive thresholding is performed. Finally the image is passed through the pytesseract wrapper function to get the text from the preprocessed image.

Future Scope: -

Security for sensitive customer information and transaction records:
Security can be ensured by recording the IP address and time stamp of the uploader. Along with that Password Encryption will also help strengthen security.

Daily Reports of the Log: -
Reports of the entire log which records all the transaction invoices processed as well as error entries which weren’t processed completely. These reports are currently generated and displayed on the website, if needed they can be mailed periodically to the company.

Daily data analytics reports: -
Reports comprising of all the data analysis carried out can also be generated and mailed to the company regularly.

Handwritten Invoice processing: -
A better trained model for more accurate extraction and structuring can be developed for handwritten text invoices.

Template personalization: -
Clients can edit templates which will be used for receipt generation. Other features such as language support, currency support, template support etc. can be integrated as well.

Presentation that explains our product further: 
https://docs.google.com/presentation/d/1yeJCOWgAZFJtHO2pS4SNIKmGq5vIMTnLCOtb4BXOZ6k/edit?usp=sharing 

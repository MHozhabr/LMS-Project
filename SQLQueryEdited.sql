create database lms;
use lms;

CREATE TABLE publishers (
	PublisherID INT PRIMARY KEY,
	PublisherName VARCHAR(255),
	PublisherAddress VARCHAR(255),
	ContactInformation VARCHAR(255)
);

CREATE TABLE members (
    MemberID INT PRIMARY KEY,
	--Password?
    MembersName VARCHAR(255),
    MembersAddress VARCHAR(255),
    Email VARCHAR(255),
    PhoneNumber VARCHAR(50),
	MemberShipType VARCHAR(255)
);

CREATE TABLE admins (
    AdminID INT PRIMARY KEY,
    UserName VARCHAR(255),
    [Password] VARCHAR(255)
);

CREATE TABLE authors (
	--book_id INT FOREIGN KEY REFERENCES Books(book_id)
	AuthorID VARCHAR(255) PRIMARY KEY,
	AuthorName VARCHAR(255),
	BirthDate DATE,
	Nationality VARCHAR(255),
	OtherRelevantInformation VARCHAR(255)
);

CREATE TABLE books (
    BookID INT PRIMARY KEY,
	AuthorID VARCHAR(255) FOREIGN KEY REFERENCES authors(AuthorID),
	Title VARCHAR(30),
	ISBN VARCHAR(30),
	PubisherID INT FOREIGN KEY REFERENCES publishers(PublisherID) ,
	Genre VARCHAR(255),
	PublicationDate DATE,
    Quantity INT,
    AvailabilityStatus VARCHAR(50)
);

CREATE TABLE transactions(
	TransactionID INT PRIMARY KEY,
	MemberID INT FOREIGN KEY REFERENCES Members(MemberID),
	BookID INT FOREIGN KEY REFERENCES Books(BookID),
	TransactionType VARCHAR(255),--BORROW OR RETURN
	TransactionDate DATE,
	DueDate DATE,
	ReturnDate DATE 
	);


CREATE TABLE latefees(
	LateFeeID INT PRIMARY KEY,
	TransactionID INT FOREIGN KEY REFERENCES Transactions(TransactionID),
	Amount INT,
	PaymentStatus VARCHAR(255),
	PaymentDate DATE
);

CREATE TABLE loans (
    LoanID INT PRIMARY KEY,
    MemberID INT,
    BookID INT,
    LoanDate DATE,
    DueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID
	)
);

	INSERT INTO publishers([PublisherID],[PublisherName],[PublisherAddress],[ContactInformation])--1
VALUES 
	(1,'jordan bark','Obere Str.57','nothing'),
	(2,'Ana Trujillo','Avda. de la Constitución 2222','nothing'),
	(3,'Antonio Moreno',' Mataderos  2312','nothing'),
	(4,'Victoria Ashworth','Fauntleroy Circus','nothing'),
	(5,'Francisco Chang','Sierras de Granada 9993','nothing');


	INSERT INTO Members (MemberID, MembersName, MembersAddress, Email, PhoneNumber)--2
VALUES
    (11,'John Smith','123 Main St','john@example.com','555-1234'),
    (22,'Jane Doe','456 Elm St','jane@example.com','555-5678'),
    (33,'David Johnson','789 Oak St','david@example.com','555-9012'),
    (44,'Emily Wilson','321 Pine St','emily@example.com','555-3456'),
    (55,'Michael Brown','654 Cedar St','michael@example.com','555-7890');


	INSERT INTO Admins (AdminID,UserName,[Password])--3
VALUES 
	(1,'admin1', 'password1'),
	(2,'admin2', 'password2'),
	(3,'admin3', 'password3'),
	(4,'admin4', 'password4'),
	(5,'admin5', 'password5');


	INSERT INTO authors([AuthorID],[AuthorName],[BirthDate],[Nationality],[OtherRelevantInformation])--4
 VALUES
	(111,'Yoshi Tannamuri','1948-12-08','USA','nothing'),
	(222,'Nancy Davolio','1948-12-08','USA','nothing'),
	(333,'Fuller Andrew','1952-02-19','USA','nothing'),
	(444,'Janet Leverting','1963-08-30','UK','nothing');


INSERT INTO Books (BookID, title, AuthorID, PublicationDate, ISBN, AvailabilityStatus)--5
VALUES
    (1111,'The Great Gatsby', 111, '1925-04-10','9780743273565','Available'),
    (2222,'To Kill a Mockingbird', 444,'1960-07-11','9780446310789','Available'),
    (3333,'1984 George Orwell', 333,'1960-07-11','9780452284234', 'On Loan'),
    (4444,'Pride and Prejudice', 222,'1813-01-28','9780141439518','Available'),
    (5555,'The Catcher in the Rye', 111,'1951-07-16','9780316769174','Available');

INSERT INTO transactions([TransactionID],[MemberID],[BookID],[TransactionType],[TransactionDate],[DueDate],[ReturnDate])--6
VALUES
      (222222,11,2222,'reserve','2023-02-15','2023-03-15','2023-03-16'),
	  (111111,22,1111,'reserve','2023-01-22','2023-02-22','2023-02-23'),
      (333333,22,3333,'reserve','2023-02-20','2023-03-20','2023-03-21'),
	  (444444,11,1111,'RERERVE','2023-04-13','2023-05-13','2023-05-14');

INSERT INTO latefees ([LateFeeID],[TransactionID],[Amount],[PaymentStatus],[PaymentDate])--7
VALUES
	(11111111,111111,5,'not payed','2023-02-23')


INSERT INTO Loans (LoanID, MemberID, BookID, LoanDate, DueDate, ReturnDate)--8
VALUES
    (11111111, 11, 2222, '2023-05-01', '2023-05-15', NULL),
    (22222222, 33, 4444, '2023-06-05', '2023-06-19', NULL),
    (33333333, 22, 1111, '2023-05-10', '2023-05-24', NULL),
    (44444444, 44, 5555, '2023-06-08', '2023-06-22', NULL),
    (55555555, 55, 3333, '2023-05-20', '2023-06-03', NULL);



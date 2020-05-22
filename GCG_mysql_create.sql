CREATE TABLE `Employee` (
	`Username` varchar(255) NOT NULL UNIQUE,
	`qualification` varchar(255) NOT NULL,
	`experience` varchar(32) NOT NULL,
	`name` varchar(255) NOT NULL,
	`email_id` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`phone_number` varchar(10) NOT NULL,
	`sector_name` varchar(255) NOT NULL,
	PRIMARY KEY (`Username`)
);

CREATE TABLE `Employer` (
	`Username` varchar(255) NOT NULL,
	`company_name` varchar(255) NOT NULL,
	`company_size` INT NOT NULL,
	`position` varchar(255) NOT NULL,
	`sector_name` varchar(255) NOT NULL,
	`sector_type` INT NOT NULL,
	`website` varchar(255),
	`email_id` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`phone_number` varchar(10) NOT NULL,
	PRIMARY KEY (`Username`)
);

CREATE TABLE `Skills` (
	`Username` varchar(255) NOT NULL,
	`skill` varchar(255) NOT NULL,
	PRIMARY KEY (`Username`)
);

CREATE TABLE `Vacancy` (
	`Username` varchar(255) NOT NULL,
	`position` varchar(255) NOT NULL,
	`skill_req` varchar(255) NOT NULL,
	PRIMARY KEY (`Username`,`position`)
);

CREATE TABLE `ContactUs` (
	`Name` varchar(255) NOT NULL,
	`email_id` varchar(255) NOT NULL,
	`subject` varchar(255) NOT NULL,
	`message` varchar(255) NOT NULL,
	PRIMARY KEY (`Name`)
);

ALTER TABLE `Skills` ADD CONSTRAINT `Skills_fk0` FOREIGN KEY (`Username`) REFERENCES `Employee`(`Username`);

ALTER TABLE `Vacancy` ADD CONSTRAINT `Vacancy_fk0` FOREIGN KEY (`Username`) REFERENCES `Employer`(`Username`);


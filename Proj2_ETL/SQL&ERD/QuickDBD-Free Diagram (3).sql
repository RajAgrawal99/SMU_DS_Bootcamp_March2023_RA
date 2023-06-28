-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/o6hVaM
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [Subcategory] (
    [subcategory_id] varchar(8)  NOT NULL ,
    [subcategory] varchar(255)  NOT NULL ,
    CONSTRAINT [PK_Subcategory] PRIMARY KEY CLUSTERED (
        [subcategory_id] ASC
    )
)

CREATE TABLE [Category] (
    [category_id] varchar(5)  NOT NULL ,
    [category] varchar(255)  NOT NULL ,
    CONSTRAINT [PK_Category] PRIMARY KEY CLUSTERED (
        [category_id] ASC
    )
)

CREATE TABLE [Contacts] (
    [contact_id] int  NOT NULL ,
    [first_name] varchar(255)  NOT NULL ,
    [last_name] varchar(255)  NOT NULL ,
    [email] varchar(255)  NOT NULL ,
    CONSTRAINT [PK_Contacts] PRIMARY KEY CLUSTERED (
        [contact_id] ASC
    )
)

CREATE TABLE [Campaign] (
    [cf_id] int  NOT NULL ,
    [contact_id] int  NOT NULL ,
    [company_name] varchar(255)  NOT NULL ,
    [description] varchar(255)  NOT NULL ,
    [goal] decimal  NOT NULL ,
    [pledged] decimal  NOT NULL ,
    [outcome] varchar(255)  NOT NULL ,
    [backers_count] int  NOT NULL ,
    [country] varchar(2)  NOT NULL ,
    [currency] varchar(3)  NOT NULL ,
    [launched_date] date  NOT NULL ,
    [end_date] date  NULL ,
    [category_id] varchar(5)  NOT NULL ,
    [subcategory_id] varchar(8)  NOT NULL ,
    CONSTRAINT [PK_Campaign] PRIMARY KEY CLUSTERED (
        [cf_id] ASC
    ),
    CONSTRAINT [UK_Campaign_contact_id] UNIQUE (
        [contact_id]
    )
)

ALTER TABLE [Subcategory] WITH CHECK ADD CONSTRAINT [FK_Subcategory_subcategory_id] FOREIGN KEY([subcategory_id])
REFERENCES [Campaign] ([subcategory_id])

ALTER TABLE [Subcategory] CHECK CONSTRAINT [FK_Subcategory_subcategory_id]

ALTER TABLE [Category] WITH CHECK ADD CONSTRAINT [FK_Category_category_id] FOREIGN KEY([category_id])
REFERENCES [Campaign] ([category_id])

ALTER TABLE [Category] CHECK CONSTRAINT [FK_Category_category_id]

ALTER TABLE [Contacts] WITH CHECK ADD CONSTRAINT [FK_Contacts_contact_id] FOREIGN KEY([contact_id])
REFERENCES [Campaign] ([contact_id])

ALTER TABLE [Contacts] CHECK CONSTRAINT [FK_Contacts_contact_id]

COMMIT TRANSACTION QUICKDBD
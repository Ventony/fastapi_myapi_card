CREATE TABLE tbl_message(
    NO              INT             AUTO_INCREAMENT PRIMARY KEY,
    NAME            VARCHAR(50)     NULL,
    EMAIL           VARCHAR(50)     NOT NULL,
    tbl_message     VARCHAR(200)    NULL,
    CREATE_DATE     DATETIME        DEFAULT CURRENT_TIMESTAMP   NULL
);
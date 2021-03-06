CREATE DATABASE IF NOT EXISTS documents;
USE documents;

DROP TABLE IF EXISTS document_controller;
DROP TABLE IF EXISTS document_creator;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS document;


CREATE TABLE document (
    id INTEGER NOT NULL AUTO_INCREMENT,
    document_name VARCHAR(50),
    document_type VARCHAR(25),
    date_of_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_of_registration TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);

CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(25),
    second_name VARCHAR(25),
    is_internal BOOLEAN,
    position VARCHAR(25),
    email VARCHAR(50),
    phone_number VARCHAR(25),

    PRIMARY KEY (id)
);

CREATE TABLE task (
    id INTEGER NOT NULL AUTO_INCREMENT,
    task_name VARCHAR(50),

    executor_id INTEGER,  /* Only one executor for one task */
    document_id INTEGER,

    FOREIGN KEY (executor_id) REFERENCES user (id),
    FOREIGN KEY (document_id) REFERENCES document (id) ON DELETE CASCADE,

    PRIMARY KEY (id)
);


CREATE TABLE document_creator (
    document_id INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,

    FOREIGN KEY (document_id) REFERENCES document (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (creator_id) REFERENCES user (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    PRIMARY KEY (document_id, creator_id)
);

CREATE TABLE document_controller (
    document_id INTEGER NOT NULL,
    controller_id INTEGER NOT NULL,

    FOREIGN KEY (document_id) REFERENCES document (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (controller_id) REFERENCES user (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    PRIMARY KEY (document_id, controller_id)
);

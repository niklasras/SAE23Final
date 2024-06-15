Schéma Relationnel
1. Étudiant
   - numero_etudiant (Primary Key)
   - nom
   - prenom
   - groupe
   - photo
   - email

2. UE (Unité d'Enseignement)
   - code (Primary Key)
   - nom
   - semestre
   - credit_ects

3. Ressource
   - code (Primary Key)
   - nom
   - descriptif
   - coefficient
   - ue_code (Foreign Key to UE)

4. Enseignant
   - id (Primary Key)
   - nom
   - prenom

5. Examen
   - id (Primary Key)
   - titre
   - date
   - coefficient
   - ue_code (Foreign Key to UE)

6. Note
   - id (Primary Key)
   - examen_id (Foreign Key to Examen)
   - etudiant_numero (Foreign Key to Étudiant)
   - note
   - appreciation




Script SQL de Création des Tables
CREATE TABLE Etudiant (
    numero_etudiant INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    groupe VARCHAR(50),
    photo VARCHAR(255),
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE UE (
    code VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    semestre VARCHAR(10) NOT NULL,
    credit_ects INT NOT NULL
);

CREATE TABLE Ressource (
    code VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    descriptif TEXT,
    coefficient DECIMAL(3, 2) NOT NULL,
    ue_code VARCHAR(10),
    FOREIGN KEY (ue_code) REFERENCES UE(code)
);

CREATE TABLE Enseignant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL
);

CREATE TABLE Examen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    coefficient DECIMAL(3, 2) NOT NULL,
    ue_code VARCHAR(10),
    FOREIGN KEY (ue_code) REFERENCES UE(code)
);

CREATE TABLE Note (
    id INT AUTO_INCREMENT PRIMARY KEY,
    examen_id INT,
    etudiant_numero INT,
    note DECIMAL(4, 2) NOT NULL,
    appreciation TEXT,
    FOREIGN KEY (examen_id) REFERENCES Examen(id),
    FOREIGN KEY (etudiant_numero) REFERENCES Etudiant(numero_etudiant)
);





Script SQL d'Insertion de Données

-- Insérer des étudiants
INSERT INTO Etudiant (nom, prenom, groupe, photo, email) VALUES
('Chouffai', 'Omar', 'RT11', 'chemin/de/photo1.jpg', 'omar.chouffai@uha.fr') ;

-- Insérer des unités d'enseignement (UE)
INSERT INTO UE (code, nom, semestre, credit_ects) VALUES
('UE102', 'Informatique', '125, 6);

-- Insérer des ressources
INSERT INTO Ressource (code, nom, descriptif, coefficient, ue_code) VALUES
('R102', 'Cours d\'Informatique', 'Descriptif du cours d\'informatique', 1.0, 'UE102');

-- Insérer des enseignants
INSERT INTO Enseignant (nom, prenom) VALUES
('Albert, 'Arnauld');

-- Insérer des examens
INSERT INTO Examen (titre, date, coefficient, ue_code) VALUES
('Examen d\'Informatique', '2024-06-02', 1.0, 'UE102');

-- Insérer des notes
INSERT INTO Note (examen_id, etudiant_numero, note, appreciation) VALUES
(2, 2, 14.0, 'Bien');

Ces scripts SQL créent les tables nécessaires pour gérer les informations des étudiants, des unités d'enseignement, des ressources, des enseignants, des examens et des notes, et insèrent des exemples de données dans ces tables.

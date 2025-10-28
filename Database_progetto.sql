-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              8.0.43 - MySQL Community Server - GPL
-- S.O. server:                  Linux
-- HeidiSQL Versione:            12.12.0.7122
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dump della struttura di tabella test_db.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria_nome` varchar(50) NOT NULL,
  `categoria_descrizione` varchar(50) NOT NULL,
  `data_creazione` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.categoria: ~2 rows (circa)
INSERT INTO `categoria` (`id`, `categoria_nome`, `categoria_descrizione`, `data_creazione`) VALUES
	(1, 'Abbigliamento', 'Cappotti', '2025-10-13'),
	(2, 'Profumeria', 'CK one', '2025-10-14'),
	(3, 'Profumeria', 'CK one', '2025-10-14');

-- Dump della struttura di tabella test_db.clienti
CREATE TABLE IF NOT EXISTS `clienti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `city` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.clienti: ~2 rows (circa)
INSERT INTO `clienti` (`id`, `first_name`, `last_name`, `city`, `age`) VALUES
	(1, 'marco', 'donatelli', 'milano', 35),
	(2, 'maria', 'redaelli', 'verona', 26);

-- Dump della struttura di tabella test_db.courses_db
CREATE TABLE IF NOT EXISTS `courses_db` (
  `id` int NOT NULL AUTO_INCREMENT,
  `corso` varchar(100) NOT NULL,
  `categoria` varchar(20) DEFAULT NULL,
  `descrizione` longtext,
  `durata_giorni` int DEFAULT '180',
  `prezzo` decimal(10,2) DEFAULT NULL,
  `data_creazione` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.courses_db: ~11 rows (circa)
INSERT INTO `courses_db` (`id`, `corso`, `categoria`, `descrizione`, `durata_giorni`, `prezzo`, `data_creazione`) VALUES
	(1, 'HTML5', 'FED', NULL, 180, 299.99, '2025-10-28 11:46:13'),
	(2, 'CSS3, Tailwind, Bootstrap', 'FED', NULL, 180, 399.99, '2025-10-28 11:46:13'),
	(3, 'JS, NODE, REACT and ANGULAR', 'FED', NULL, 180, 599.99, '2025-10-28 11:46:13'),
	(4, 'PHP con LARAVEL', 'BED', NULL, 180, 449.99, '2025-10-28 11:46:13'),
	(5, 'Python con Flask e Django', 'BED', NULL, 180, 499.99, '2025-10-28 11:46:13'),
	(6, 'JAVA', 'BED', NULL, 180, 549.99, '2025-10-28 11:46:13'),
	(7, 'Database con MySQL', 'BED', NULL, 180, 349.99, '2025-10-28 11:46:13'),
	(8, 'Linux', 'OTHER', NULL, 180, 199.99, '2025-10-28 11:46:13'),
	(9, 'Bash', 'OTHER', NULL, 180, 149.99, '2025-10-28 11:46:13'),
	(10, 'Cybersecurity', 'OTHER', NULL, 180, 399.99, '2025-10-28 11:46:13'),
	(11, 'Ethical Hacking', 'OTHER', NULL, 180, 299.99, '2025-10-28 11:46:13');

-- Dump della struttura di tabella test_db.iscritti
CREATE TABLE IF NOT EXISTS `iscritti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.iscritti: ~0 rows (circa)

-- Dump della struttura di tabella test_db.iscrizioni_db
CREATE TABLE IF NOT EXISTS `iscrizioni_db` (
  `id` int NOT NULL AUTO_INCREMENT,
  `utente_id` int NOT NULL,
  `corso_id` int NOT NULL,
  `ruolo` enum('ADMIN','STUDENTE') NOT NULL,
  `data_iscrizione` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `completato` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unico_utente_corso` (`utente_id`,`corso_id`),
  KEY `corso_id` (`corso_id`),
  CONSTRAINT `iscrizioni_db_ibfk_1` FOREIGN KEY (`utente_id`) REFERENCES `users_db` (`id`) ON DELETE CASCADE,
  CONSTRAINT `iscrizioni_db_ibfk_2` FOREIGN KEY (`corso_id`) REFERENCES `courses_db` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.iscrizioni_db: ~0 rows (circa)

-- Dump della struttura di tabella test_db.prodotti
CREATE TABLE IF NOT EXISTS `prodotti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_prodotto` varchar(50) NOT NULL,
  `prezzo` int NOT NULL,
  `in_offerta` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_categoria` (`category_id`),
  CONSTRAINT `fk_categoria` FOREIGN KEY (`category_id`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.prodotti: ~2 rows (circa)
INSERT INTO `prodotti` (`id`, `nome_prodotto`, `prezzo`, `in_offerta`, `category_id`) VALUES
	(1, 'formaggio', 5, 1, 1);

-- Dump della struttura di tabella test_db.users_db
CREATE TABLE IF NOT EXISTS `users_db` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `data_registrazione` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ruolo` varchar(50) NOT NULL DEFAULT 'UTENTE',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump dei dati della tabella test_db.users_db: ~2 rows (circa)
INSERT INTO `users_db` (`id`, `nome`, `cognome`, `email`, `pwd`, `data_registrazione`, `ruolo`) VALUES
	(1, 'Fabrizio', 'Guzzetta', 'fabrizio.guzzetta@gmail.com', 'Lafamenera1', '2025-10-16 13:51:38', 'ADMIN'),
	(2, 'Fabrizio', 'Guzzetta', 'bluedragon79@hotmail.it', 'Lafamenera', '2025-10-16 13:58:29', 'UTENTE');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

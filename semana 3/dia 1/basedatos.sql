-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_sistemapos
CREATE DATABASE IF NOT EXISTS `db_sistemapos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `db_sistemapos`;

-- Volcando estructura para tabla db_sistemapos.cat_producto
CREATE TABLE IF NOT EXISTS `cat_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Categoria de productos';

-- Volcando datos para la tabla db_sistemapos.cat_producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `cat_producto` DISABLE KEYS */;
INSERT INTO `cat_producto` (`id`, `nombre`) VALUES
	(1, 'PC'),
	(2, 'laptop');
/*!40000 ALTER TABLE `cat_producto` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Tipo de Documento',
  `tipo_doc_ide` int(11) NOT NULL DEFAULT '0' COMMENT 'Referencia a la tabla tiop_doc_ide',
  `nro_doc` varchar(20) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_documento` (`tipo_doc_ide`,`nro_doc`),
  CONSTRAINT `FK_clientes_tipo_doc_ide` FOREIGN KEY (`tipo_doc_ide`) REFERENCES `tipo_doc_ide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Registra los clientes del sistema';

-- Volcando datos para la tabla db_sistemapos.clientes: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `tipo_doc_ide`, `nro_doc`, `nombre`, `telefono`, `correo`) VALUES
	(1, 1, '75584292', 'alex', '978123876', 'ale@email.com'),
	(2, 2, '1075584932', 'Alex EIRL', '01 75543621', 'soluciones@alex.pe');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_producto_id` int(11) NOT NULL DEFAULT '0',
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `marca` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `modelo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nro_serie` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `mem_ram` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `procesador` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `disco_duro` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_producto_cat_producto_id` (`cat_producto_id`),
  CONSTRAINT `fk_producto_cat_producto_id` FOREIGN KEY (`cat_producto_id`) REFERENCES `cat_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='producto';

-- Volcando datos para la tabla db_sistemapos.producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` (`id`, `cat_producto_id`, `nombre`, `marca`, `modelo`, `nro_serie`, `mem_ram`, `procesador`, `disco_duro`, `precio`, `stock`) VALUES
	(1, 1, 'PC CORE I5 Estudiante', 'LENOVO', '5100', '34434FF43', '8GB', 'CORE I5 10', '1 TB', 3500.00, 20),
	(2, 2, 'DELL INSPIRON 5000', 'DELL', 'INSPIRON', '12Q21', '16GB', 'CORE I7 11', '1 TB', 4500.00, 5);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL DEFAULT '0',
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  `precio` decimal(10,2) NOT NULL DEFAULT '0.00',
  `stock` bigint(20) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla db_sistemapos.productos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.tipo_doc_ide
CREATE TABLE IF NOT EXISTS `tipo_doc_ide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='tipo de documento de indentidad';

-- Volcando datos para la tabla db_sistemapos.tipo_doc_ide: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `tipo_doc_ide` DISABLE KEYS */;
INSERT INTO `tipo_doc_ide` (`id`, `nombre`) VALUES
	(1, 'DNI'),
	(2, 'RUC\r\n'),
	(3, 'CARNET EXTRANJERIA');
/*!40000 ALTER TABLE `tipo_doc_ide` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

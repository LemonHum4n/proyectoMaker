-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_maker
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_maker
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_maker` DEFAULT CHARACTER SET utf8 ;
USE `esquema_maker` ;

-- -----------------------------------------------------
-- Table `esquema_maker`.`classrooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_maker`.`zone` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_maker`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_maker`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(200) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;




-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


create table if not exists `esquema_maker`.`horario`(
	 `id` INT NOT NULL AUTO_INCREMENT,
	 `hora` varchar(46) not null ,
    primary key(`id`)
);



-- -----------------------------------------------------
-- Table `esquema_maker`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_maker`.`reserva` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rut` VARCHAR(20) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `tipo_visita` VARCHAR(45) NOT NULL,
  `zone_id` INT NOT NULL,
  `fecha_reserva` DATE NOT NULL,
  `horario_id` int NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_reserva_user_idx` (`user_id` ASC),
  INDEX `fk_reserva_zone_idx` (`zone_id` ASC),
  CONSTRAINT `fk_reserva_zone`
    FOREIGN KEY (`zone_id`)
    REFERENCES `esquema_maker`.`zone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
	  constraint `fk_horario` 
	 foreign key(`horario_id`)
      references `esquema_maker`.`horario`(`id`)
      on delete cascade
      on update cascade)
ENGINE = InnoDB;



insert into horario values (1,'08:00');
insert into horario values (2,'09:00');
insert into horario values (3,'10:00');
insert into horario values (4,'11:00');
insert into horario values (5,'12:00');
insert into horario values (6,'13:00');
insert into horario values (7,'14:00');
insert into horario values (8,'15:00');
insert into horario values (9,'16:00');

select * from horario;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

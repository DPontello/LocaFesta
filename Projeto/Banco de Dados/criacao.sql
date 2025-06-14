-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `nomeCliente` VARCHAR(100) NOT NULL,
  `emailCliente` VARCHAR(100) NOT NULL,
  `telefoneCliente` VARCHAR(19) NOT NULL,
  `cpfCnpjCliente` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE INDEX `emailCliente_UNIQUE` (`emailCliente` ASC) VISIBLE,
  UNIQUE INDEX `telefoneCliente_UNIQUE` (`telefoneCliente` ASC) VISIBLE,
  UNIQUE INDEX `cpfCnpj_UNIQUE` (`cpfCnpjCliente` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`equipamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`equipamento` (
  `idEquipamento` INT NOT NULL AUTO_INCREMENT,
  `nomeEquipamento` VARCHAR(100) NOT NULL,
  `tipoEquipamento` VARCHAR(100) NOT NULL,
  `valorDiaria` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`idEquipamento`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reserva` (
  `idReserva` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idEquipamento` INT NOT NULL,
  `dataInicio` DATE NOT NULL,
  `dataFim` DATE NOT NULL,
  `status` ENUM('Ativa', 'Finalizada', 'Cancelada') NOT NULL,
  PRIMARY KEY (`idReserva`, `idCliente`, `idEquipamento`),
  INDEX `fk_reserva_cliente_idx` (`idCliente` ASC) VISIBLE,
  INDEX `fk_reserva_equipamento1_idx` (`idEquipamento` ASC) VISIBLE,
  CONSTRAINT `fk_reserva_cliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `mydb`.`cliente` (`idCliente`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reserva_equipamento1`
    FOREIGN KEY (`idEquipamento`)
    REFERENCES `mydb`.`equipamento` (`idEquipamento`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionario` (
  `idFuncionario` INT NOT NULL,
  `nomeFuncionario` VARCHAR(100) NOT NULL,
  `emailFuncionario` VARCHAR(100) NOT NULL,
  `telefoneFuncionario` VARCHAR(19) NOT NULL,
  `senhaFuncionario` VARCHAR(200) NOT NULL,
  `ehAdmin` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idFuncionario`),
  UNIQUE INDEX `emailFuncionario_UNIQUE` (`emailFuncionario` ASC) VISIBLE,
  UNIQUE INDEX `telefoneFuncionario_UNIQUE` (`telefoneFuncionario` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

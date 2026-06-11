
CREATE SCHEMA IF NOT EXISTS `sistema_biblioteca_banco` DEFAULT CHARACTER SET utf8 ;
USE `sistema_biblioteca_banco` ;


CREATE TABLE IF NOT EXISTS `sistema_biblioteca_banco`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(20) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `perfil` ENUM('administrador', 'funcionario', 'cliente'),
  PRIMARY KEY (`idusuario`),
  UNIQUE INDEX `telefone_UNIQUE` (`telefone` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `sistema_biblioteca_banco`.`livro` (
  `idlivro` INT NOT NULL AUTO_INCREMENT,
  `isbn` VARCHAR(13) NOT NULL,
  `titulo` VARCHAR(255) NOT NULL,
  `autor` VARCHAR(100) NOT NULL,
  `editora` VARCHAR(100) NOT NULL,
  `ano_publicacao` INT NOT NULL,
  `status` ENUM('disponivel', 'indisponivel') NOT NULL DEFAULT 'disponivel',
  PRIMARY KEY (`idlivro`),
  UNIQUE INDEX `isbn_UNIQUE` (`isbn` ASC),
  UNIQUE INDEX `titulo_UNIQUE` (`titulo` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `sistema_biblioteca_banco`.`usuario_has_livro` (
  `usuario_idusuario` INT NOT NULL,
  `livro_idlivro` INT NOT NULL,
  `data_emprestimo` DATE NOT NULL,
  `data_devolucao` DATE NOT NULL,
  PRIMARY KEY (`usuario_idusuario`, `livro_idlivro`),
  INDEX `fk_usuario_has_livro_livro1_idx` (`livro_idlivro` ASC),
  INDEX `fk_usuario_has_livro_usuario_idx` (`usuario_idusuario` ASC),
  CONSTRAINT `fk_usuario_has_livro_usuario`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `sistema_biblioteca_banco`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuario_has_livro_livro1`
    FOREIGN KEY (`livro_idlivro`)
    REFERENCES `sistema_biblioteca_banco`.`livro` (`idlivro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



const {
    validateStrings,
    validateCpfCnpj,
    validateEmail,
    validatePhone,
    validateValorDiaria,
    validateSelect,
    validateDataInicioFim,
    validateStatus
} = require('./validations');

// Testes unitários para funções de validação

describe('Validações Gerais', () => {
    it('validateStrings deve retornar true para strings válidas', () => {
        expect(validateStrings('Teste')).toBe(true);
    });

    it('validateStrings deve retornar false para strings inválidas', () => {
        expect(validateStrings('')).toBe(false);
    });
});

describe('Validação de CPF/CNPJ', () => {
    it('CPF válido deve passar', () => {
        expect(validateCpfCnpj('123.456.789-00')).toBe(true);
    });

    it('CNPJ válido deve passar', () => {
        expect(validateCpfCnpj('12.345.678/0001-90')).toBe(true);
    });

    it('Entrada inválida deve falhar', () => {
        expect(validateCpfCnpj('abc')).toBe(false);
    });
});

describe('Validação de Email', () => {
    it('Email válido deve passar', () => {
        expect(validateEmail('teste@exemplo.com')).toBe(true);
    });

    it('Email inválido deve falhar', () => {
        expect(validateEmail('teste@')).toBe(false);
    });
});

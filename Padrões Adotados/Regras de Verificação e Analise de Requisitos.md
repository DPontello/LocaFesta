# Regras de Verificação e Análise de Requisitos

## Nomenclatura dos Requisitos

Os requisitos serão identificados utilizando a seguinte padronização:

- **RF-XX** – Requisito Funcional  
  > Exemplo: RF-01 – O sistema deve permitir o cadastro de novos clientes.

- **RNF-XX** – Requisito Não Funcional  
  > Exemplo: RNF-01 – O sistema deve ter tempo de resposta inferior a 2 segundos para operações de reserva.

Os requisitos serão numerados sequencialmente conforme forem identificados.

---

## Regras para o Documento de Requisitos

A documentação dos requisitos seguirá os princípios de qualidade descritos no **Capítulo 1 do livro de Rogério Magela**, respeitando as seguintes regras:

### 1. **Clareza**
Os requisitos devem ser expressos de forma objetiva e sem ambiguidades.

**✅ Exemplo com bom uso de clareza:**  
> RF-05 – O sistema deve permitir que funcionários alterem a data de uma reserva existente.

**❌ Exemplo ruim:**  
> “O sistema deve ser fácil de usar.”

### 2. **Consistência**
Requisitos não podem se contradizer ou gerar dúvidas quanto ao comportamento esperado.

**✅ Exemplo consistente:**  
> RF-08 – O sistema não deve permitir reservas de equipamentos indisponíveis no estoque.

**❌ Exemplo contraditório:**  
> Um requisito que diz que "o sistema sempre deve aceitar reservas" contradiz o acima.

### 3. **Verificabilidade**
Deve ser possível testar ou inspecionar o requisito para confirmar seu atendimento.

**✅ Exemplo verificável:**  
> RNF-03 – O sistema deve suportar até 20 acessos simultâneos sem queda de desempenho.

**❌ Exemplo vago:**  
> “O sistema deve funcionar bem com muitos usuários.”

### 4. **Prioridade**
Requisitos devem ser classificados por sua importância: **obrigatórios**, **desejáveis** ou **opcionais**.

**✅ Exemplo com prioridade:**  
> RF-15 – (Obrigatório) O sistema deve permitir login com autenticação via senha criptografada.

### 5. **Completude**
O requisito deve conter todas as informações necessárias para ser entendido e implementado.

**✅ Exemplo de requisito completo:**  
> RF-12 – O sistema deve enviar um e-mail de confirmação para o cliente até 5 minutos após a efetivação da reserva.
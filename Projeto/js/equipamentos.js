// CRUD de equipamentos

let editingEquipamentoId = null;

// Carrega a lista de equipamentos na tabela
async function loadEquipamentos() {
    const tableBody = document.getElementById('equipamentosTableBody');
    tableBody.innerHTML = `<tr><td colspan="5"><i class="fas fa-spinner fa-spin me-2"></i>Carregando equipamentos...</td></tr>`;
    try {
        const equipamentos = await apiRequest('/equipamentos');
        if (equipamentos.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" class="text-center">Nenhum equipamento encontrado.</td></tr>`;
            return;
        }
        tableBody.innerHTML = '';
        equipamentos.forEach(equip => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${equip.idEquipamento}</td>
                <td>${equip.nomeEquipamento}</td>
                <td>${equip.tipoEquipamento}</td>
                <td>R$ ${parseFloat(equip.valorDiaria).toFixed(2)}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="editEquipamento(${equip.idEquipamento})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteEquipamento(${equip.idEquipamento})">Deletar</button>
                </td>`;
            tableBody.appendChild(row);
        });
    } catch (error) {
        tableBody.innerHTML = `<tr><td colspan="5" class="text-danger">Erro ao carregar equipamentos.</td></tr>`;
        console.error('Erro ao carregar equipamentos:', error);
    }
}

// Abre o modal para adicionar um equipamento novo
function showAddEquipamentoModal() {
    editingEquipamentoId = null;
    document.getElementById('equipamentoModalTitle').textContent = 'Adicionar Equipamento';
    document.getElementById('equipamentoForm').reset();
    new bootstrap.Modal(document.getElementById('equipamentoModal')).show();
}

// Abre o modal para editar equipamento existente
async function editEquipamento(id) {
    try {
        const equipamento = await apiRequest(`/equipamentos/${id}`);
        editingEquipamentoId = id;
        document.getElementById('equipamentoModalTitle').textContent = 'Editar Equipamento';
        document.getElementById('nomeEquipamento').value = equipamento.nomeEquipamento;
        document.getElementById('tipoEquipamento').value = equipamento.tipoEquipamento;
        document.getElementById('valorDiaria').value = equipamento.valorDiaria;
        new bootstrap.Modal(document.getElementById('equipamentoModal')).show();
    } catch (error) {
        alert('Erro ao carregar equipamento: ' + error.message);
        console.error(error);
    }
}

// Salva equipamento (novo ou editado)
async function saveEquipamento() {
    const nome = document.getElementById('nomeEquipamento').value.trim();
    const tipo = document.getElementById('tipoEquipamento').value.trim();
    const valor = parseFloat(document.getElementById('valorDiaria').value);

    const equipamentoData = {
        nomeEquipamento: nome,
        tipoEquipamento: tipo,
        valorDiaria: valor
    };

    try {
        if (editingEquipamentoId) {
            await apiRequest(`/equipamentos/${editingEquipamentoId}`, 'PUT', equipamentoData);
            alert('Equipamento atualizado com sucesso!');
        } else {
            await apiRequest('/equipamentos', 'POST', equipamentoData);
            alert('Equipamento adicionado com sucesso!');
        }
        bootstrap.Modal.getInstance(document.getElementById('equipamentoModal')).hide();
        await loadEquipamentos();
    } catch (error) {
        alert('Erro ao salvar equipamento: ' + error.message);
    }
}

// Deleta equipamento
async function deleteEquipamento(id) {
    if (confirm('Deseja excluir este equipamento?')) {
        try {
            await apiRequest(`/equipamentos/${id}`, 'DELETE');
            alert('Equipamento excluído com sucesso!');
            await loadEquipamentos();
        } catch (error) {
            alert('Erro ao excluir equipamento: ' + error.message);
        }
    }
}

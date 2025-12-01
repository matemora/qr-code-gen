# Gerador de QR Code

Uma aplicação web simples construída com Flask que gera QR codes a partir de texto. Digite qualquer texto, URL ou informação e obtenha instantaneamente uma imagem de QR code escaneável.

## Funcionalidades

- 🎯 Interface web simples e intuitiva
- ⚡ Geração instantânea de QR code
- 🖼️ Exibe QR codes diretamente no navegador
- 📱 Funciona com qualquer texto, URLs, informações de contato, etc.
- 🎨 Design limpo e moderno

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. **Clone ou baixe este projeto**

2. **Crie um ambiente virtual (recomendado)**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**

   No Windows:
   ```bash
   venv\Scripts\activate
   ```

   No Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```
   
## Uso

1. **Execute a aplicação**

   ```bash
   python main.py
   ```

2. **Abra seu navegador**

   Navegue para: `http://localhost:5000`

3. **Gere QR codes**

   - Digite qualquer texto ou URL no campo de entrada
   - Clique em "Gerar QR Code"
   - Seu QR code aparecerá na tela
   - Escaneie com seu celular para testar!

## Estrutura do Projeto

```
qr-code-gen/
│
├── main.py           # Aplicação Flask principal
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## Dependências

- **Flask** - Framework web para Python
- **qrcode** - Biblioteca de geração de QR code
- **Pillow** - Biblioteca de processamento de imagem (necessária para saída PNG)

## Como Funciona

1. O backend Flask serve um formulário HTML com CSS incorporado
2. O usuário digita o texto e envia o formulário
3. O backend gera um QR code usando a biblioteca `qrcode`
4. O QR code é armazenado na memória como uma imagem PNG
5. A imagem é exibida na página web

## Exemplos do Que Você Pode Codificar

- URLs de sites: `https://example.com`
- Informações de contato: `João Silva, joao@example.com, +5511987654321`
- Credenciais WiFi: `WIFI:T:WPA;S:NomeDaRede;P:Senha;;`
- Mensagens de texto simples
- Números de telefone: `tel:+5511987654321`
- Endereços de email: `mailto:email@example.com`

## Solução de Problemas

### Porta já em uso
Se a porta 5000 já estiver ocupada, modifique a última linha em `main.py`:
```python
app.run(debug=True, port=5001)  # Use uma porta diferente
```

### Problemas de instalação no Mac
Use aspas ao redor do nome do pacote:
```bash
pip install 'qrcode[pil]'
```

### QR code não está sendo exibido
Certifique-se de que as rotas `/generate` e `/qr_image` estão funcionando. Verifique o console do navegador para erros.

## Personalização

Você pode personalizar a aparência do QR code na função `generate()`:

```python
qr = qrcode.QRCode(
    version=1,              # Tamanho (1-40, maior = maior)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
    box_size=10,            # Tamanho do pixel de cada caixa
    border=4,               # Espessura da borda
)
```

## Melhorias Futuras

- Baixar QR code como arquivo PNG
- Personalizar cores do QR code
- Ajustar tamanho do QR code
- Gerar múltiplos QR codes em lote
- Adicionar histórico de QR codes

## Licença

Este projeto é livre para uso e modificação para fins pessoais e comerciais.

## Contribuindo

Sinta-se à vontade para fazer um fork deste projeto e enviar pull requests com melhorias!

## Suporte

Se você encontrar algum problema, verifique a seção de Solução de Problemas ou abra uma issue no repositório do projeto.

---

**Aproveite para gerar QR codes!** 📱✨

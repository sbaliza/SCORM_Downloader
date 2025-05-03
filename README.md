# SCORM Downloader

Este script em Python automatiza o download de todos os arquivos referenciados em um pacote SCORM através do manifesto `imsmanifest.xml`, mantendo a estrutura original de diretórios e decodificando corretamente os nomes dos arquivos.

---

## 📚 Sobre SCORM

SCORM (Sharable Content Object Reference Model) é um padrão para criação de objetos de aprendizado reutilizáveis e interoperáveis, comumente utilizado em plataformas de ensino a distância (LMS - Learning Management Systems).

### O que é um manifesto SCORM?

Todo pacote SCORM é um arquivo compactado (ZIP) contendo um manifesto (`imsmanifest.xml`) na raiz. Este manifesto:

- Define a estrutura do conteúdo (módulos, páginas, quizzes, etc.).
- Lista todos os arquivos necessários para execução (HTML, JS, imagens, etc.).
- Contém referências para os arquivos via atributos `href`.

Este script utiliza o manifesto para localizar e baixar todos os arquivos referenciados de forma automática, mantendo a estrutura de diretórios definida.

---

## 📦 Requisitos

- Python 3.6+
- Pacotes Python:
  - `requests`
  - `beautifulsoup4`
  - `tqdm`

### Instalação dos pacotes

```bash
pip install requests beautifulsoup4 tqdm
```

---

## 🚀 Uso

```bash
python3 scorm_downloader.py --manifest URL_DO_MANIFESTO [--output DIRETORIO_DESTINO]
```

### Parâmetros

- `--manifest`: **(Obrigatório)** URL completa para o arquivo `imsmanifest.xml` de um pacote SCORM hospedado.
- `--output`: (Opcional) Diretório base local onde os arquivos serão salvos. O padrão é o diretório atual (`.`).

---

## 💡 Exemplo

```bash
python3 scorm_downloader.py \
  --manifest https://www.portal.com/courses/6541_SHORT/scorms/Chap01_scorm01/imsmanifest.xml \
  --output ./downloads
```

O exemplo acima irá:

- Ler o arquivo `imsmanifest.xml` remoto.
- Identificar todos os arquivos referenciados por `href`.
- Fazer o download desses arquivos mantendo a estrutura original de pastas (ex: `6541_SHORT/scorms/Chap01_scorm01/scormdriver/file.html`).
- Decodificar corretamente nomes de arquivos com caracteres escapados (ex: `Image_10%20RED` → `Image_10 RED`).

---

## ✅ Funcionalidades

- ✅ Preserva a estrutura de diretórios conforme definido no `href` do manifesto.
- ✅ Decodifica nomes de arquivos (`urldecode`) para salvar com nomes legíveis.
- ✅ Exibe barra de progresso para cada arquivo baixado.
- ✅ Tolerante a erros em downloads individuais.
- ✅ Pronto para automações e pipelines de ingestão SCORM.

---

## 🛡️ Considerações

- Este script **não realiza validação semântica** dos arquivos ou das regras SCORM — seu foco é a replicação fiel dos arquivos referenciados.
- É recomendado verificar a integridade e funcionamento do conteúdo baixado em um ambiente LMS antes de usa-lo.

---

Desenvolvido para facilitar a criação de treinamentos a partir de treinamentos existes e a possibilidade de consumir um conteúdo de outro idioma no seu idioma nativo de forma facilitada.


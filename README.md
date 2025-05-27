# Visual Content Search Engine

A powerful image search system that allows users to find images based on their visual content using AI vision capabilities and RAG (Retrieval Augmented Generation).

## 🌟 Features

- **Image Upload**: Upload multiple images to build your searchable database
- **AI-Powered Content Analysis**: Automatic analysis of image content using advanced vision AI
- **Semantic Search**: Search for images using natural language descriptions
- **Local RAG Storage**: Efficient local storage of image embeddings and metadata
- **Fast Retrieval**: Quick and accurate retrieval of similar images
- **User-Friendly Interface**: Simple and intuitive web interface

## 🏗️ Architecture

The system consists of the following components:

1. **Frontend Interface**
   - Web-based upload interface
   - Search interface
   - Results visualization

2. **Backend Services**
   - Image processing service
   - Vision AI integration
   - RAG (Retrieval Augmented Generation) system
   - Search engine

3. **Storage**
   - Local vector database for embeddings
   - Image metadata storage
   - Original image storage

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- GPU (recommended for faster processing)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/search-through-images.git
cd search-through-images
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

1. Start the backend server:
```bash
python server.py
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Access the application at `http://localhost:3000`

## 💡 How It Works

1. **Image Upload Process**
   - Users upload images through the web interface
   - Each image is processed by the Vision AI model
   - Visual content is analyzed and converted into embeddings
   - Embeddings and metadata are stored in the local RAG system

2. **Search Process**
   - Users enter natural language queries
   - The system converts the query into a compatible embedding
   - RAG system retrieves the most similar images
   - Results are ranked and displayed to the user

## 🛠️ Technical Stack

- **Frontend**: React.js, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI
- **Vision AI**: OpenAI Vision API
- **Vector Database**: ChromaDB
- **Image Processing**: PIL, OpenCV
- **RAG Implementation**: LangChain

## 📝 API Documentation

### Endpoints

- `POST /api/upload`: Upload images
- `POST /api/search`: Search for images
- `GET /api/images`: Retrieve image list
- `GET /api/image/:id`: Get specific image details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for Vision API
- LangChain community
- ChromaDB team 
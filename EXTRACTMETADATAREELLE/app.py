
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from PyPDF2 import PdfFileReader

from docx import Document
from openpyxl import load_workbook
from pptx import Presentation
from PIL import Image
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
all_file_metadata = []

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    if 'folder' in request.files:
        uploaded_files = request.files.getlist('folder')

        # Assurez-vous que le dossier temporaire existe
        temp_folder = UPLOAD_FOLDER
        os.makedirs(temp_folder, exist_ok=True)

        # Enregistrez chaque fichier dans le dossier temporaire
        for uploaded_file in uploaded_files:
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(temp_folder, filename)
            uploaded_file.save(file_path)

        # Nettoyez la liste des métadonnées avant d'ajouter de nouvelles données
        all_file_metadata.clear()

        # Parcourez tous les fichiers du dossier temporaire et extrayez les métadonnées
        for root, dirs, files in os.walk(temp_folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                metadata = extract_metadata(file_path)
                if metadata:
                    # Ajoutez les métadonnées à la liste
                    all_file_metadata.append({'file_name': file_name, 'metadata': metadata})

        # Redirigez vers la page de métadonnées
        return redirect(url_for('metadata', folder_path=temp_folder))
    else:
        return render_template('index.html', error="No folder selected")


@app.route('/metadata/<folder_path>')
def metadata(folder_path):
    return render_template('metadata.html', all_file_metadata=all_file_metadata)
def simple_convert(metadata):
    if isinstance(metadata, dict):
        return {k: str(v) for k, v in metadata.items()}
    elif isinstance(metadata, list):
        return [str(elem) for elem in metadata]
    else:
        return str(metadata)

@app.route('/metadata_data')
def metadata_data():
    for item in all_file_metadata:
        print(item)  # Log pour inspecter les données
   
    return jsonify(simple_convert(all_file_metadata))



def extract_docx_metadata(file_path):
    doc = Document(file_path)
    docx_metadata = {
        'Title': doc.core_properties.title,
        'Author': doc.core_properties.author,
        'Created': doc.core_properties.created,
        'Modified': doc.core_properties.modified,
    }
    return docx_metadata


def extract_xlsx_metadata(file_path):
    excel_doc = load_workbook(file_path)
    properties = excel_doc.properties
    xlsx_metadata = {
        'Title': properties.title,
        'Author': properties.author,
        'Created': properties.created,
        'Modified': properties.modified,
    }
    return xlsx_metadata

def extract_pptx_metadata(file_path):
    pptx_doc = Presentation(file_path)
    pptx_metadata = {
        'Title': pptx_doc.core_properties.title,
        'Author': pptx_doc.core_properties.author,
        'Created': pptx_doc.core_properties.created,
        'Modified': pptx_doc.core_properties.modified,
    }
    return pptx_metadata
def extract_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        info = pdf_reader.getDocumentInfo()
        return simple_convert(info)        
def extract_image_metadata(image_path):
    with Image.open(image_path) as img:
        image_metadata = {
            'Format': img.format,
            'Mode': img.mode,
            'Size': img.size,
            'Info': img.info,
            # Ajoutez d'autres métadonnées en fonction de vos besoins
        }
    return image_metadata


#def extract_audio_metadata(audio_path):
  #  audio = AudioSegment.from_file(audio_path)
    
    #audio_metadata = {
        #'Channels': audio.channels,
       # 'Sample Width': audio.sample_width,
        #'Frame Rate': audio.frame_rate,
       # 'Frame Width': audio.frame_width,
        #'Length (ms)': len(audio),
        #'Tags': audio.tags,  # Vous pouvez personnaliser cela en fonction de ce que vous voulez extraire
   # }
    
    #return audio_metadata
from moviepy.editor import VideoFileClip

def extract_video_metadata(video_path):
    clip = VideoFileClip(video_path)
    
    video_metadata = {
        'Duration (s)': clip.duration,
        'Size': clip.size,
        'FPS': clip.fps,
        # Ajoutez d'autres métadonnées en fonction de vos besoins
    }
    
    return video_metadata

def extract_metadata(file_path):
    file_extension = file_path.split('.')[-1].lower()
    supported_extensions = ['docx', 'xlsx', 'pptx', 'pdf', 'jpg', 'jpeg', 'png', 'gif', 'mp3', 'wav', 'mp4', 'avi', 'mkv']

    if file_extension in supported_extensions:
        if file_extension == 'docx':
            return extract_docx_metadata(file_path)
        elif file_extension == 'xlsx':
            return extract_xlsx_metadata(file_path)
        elif file_extension == 'pptx':
            return extract_pptx_metadata(file_path)
        elif file_extension == 'pdf':
            return extract_pdf_metadata(file_path)
        elif file_extension in ['jpg', 'jpeg', 'png', 'gif']:
            return extract_image_metadata(file_path)
       # elif file_extension in ['mp3', 'wav']:
        #    return extract_audio_metadata(file_path)
        elif file_extension in ['mp4', 'avi', 'mkv']:
            return extract_video_metadata(file_path)
    else:
        return None
if __name__ == '__main__':
    app.run(debug=True)

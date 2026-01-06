from pathlib import Path

from dstvparser.parsers.factory import NCFileParserFactory
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstv_tools.exporters.profile_dxf_exporter import ProfileDXFExporter  

if __name__ == '__main__':
    nc_path = Path(__file__).parent / "data" / "722.nc"

    if nc_path.exists():
        print("File trovato!")
    else:
        print("File NON trovato!")
        exit(1)
        
    # Parse del file NC
    nc_part = NCFileParserFactory.create_parser(nc_path)
    profile = nc_part.parse()

    # Composizione delle facce del profilo
    profile_faces = ComposeProfileFaces(profile)
    
    # Crea l'esportatore DXF
    exporter = ProfileDXFExporter(profile_faces)
    
    # Esempio 1: Esporta una singola faccia (flangia superiore)
    print("\n--- Esportazione singola faccia 'o' (flangia superiore) ---")
    file_single = exporter.export_face('o', add_labels=True)
    print(f"File esportato: {file_single}")
    
    # Esempio 2: Esporta tutte le facce in file separati
    print("\n--- Esportazione facce separate ---")
    output_dir = Path(__file__).parent.parent
    base_path = output_dir / "profilo_722"
    files_separate = exporter.export_all_faces(
        base_file_path=str(base_path), 
        separate_files=True, 
        add_labels=True
    )
    print(f"File esportati:")
    for f in files_separate:
        print(f"  - {f}")
    
    # Esempio 3: Esporta tutte le facce in un unico file con offset
    print("\n--- Esportazione facce in un unico file ---")

    profile_faces = ComposeProfileFaces(profile, offset_between_faces=150)

    exporter = ProfileDXFExporter(profile_faces)

    file_complete = exporter.export_all_faces(
        base_file_path=str(base_path), 
        separate_files=False, 
        add_labels=True
    )
    print(f"File completo esportato: {file_complete}")
    
    print("\n✓ Esportazione completata con successo!")


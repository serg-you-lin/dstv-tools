from pathlib import Path

#from dstv_parser.DSTVParser.parsers.factory import NCFileParserFactory
from dstvparser.parsers.factory import NCFileParserFactory
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstv_tools.plotters.profile_plotter import ProfilePlotter

if __name__ == '__main__':
    # Path relativo al file corrente
    nc_path = Path(__file__).parent.parent / "examples" / "data" / "722.nc"

    if nc_path.exists():
        print("File trovato!")
    else:
        print("File NON trovato!")
        
    nc_part = NCFileParserFactory.create_parser(nc_path)
    profile = nc_part.parse()

    profile_faces = ComposeProfileFaces(profile)
    plotter = ProfilePlotter(profile_faces)
    # plotter.plot_face('o')
    plotter.plot_all_faces()
    plotter.show()
    # plotter.save('profile_plot.png')

    
from pathlib import Path
import sys


from dstv_tools.plotters.interactive_plotter import InteractiveProfilePlotter
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstvparser.parsers.factory import NCFileParserFactory
from dstvparser.parsers.nc_file_parser import *

if __name__ == '__main__':
    nc_path = Path(__file__).parent.parent / "examples" / "data" / "722.nc"

    part_nc = NCFileParserFactory.create_parser(nc_path)
    profile = part_nc.parse()

    profile_faces = ComposeProfileFaces(profile, offset_between_faces=000)

    plotter = InteractiveProfilePlotter(profile_faces, y_plot_lim=150)
    fig = plotter.plot_all_faces(with_offset=True)
    # fig = plotter.plot_face('o')
    plotter.show(fig)

    # plotter.save('profile_plot.png')








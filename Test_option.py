from optparse import OptionParser
import sys
def main():
    parser = OptionParser(usage="usage: %prog -i <story_header.csv> -s <story_header_sell_all.csv>",
                          version="%prog 1.0")

    parser.add_option("-i", "--input",
                      action="store",
                      dest="inputfile",
                      type="string",
                      help="Filename of story_header -- type(csv)")

    parser.add_option("-s", "--sell",
                      action="store", # optional because action defaults to "store"
                      dest="inputfile_seller",
                      type="string",
                      help="Filename of story_header_sell_all -- type(csv)")

    parser.add_option("-o", "--output",
                      action="store", # optional because action defaults to "store"
                      dest="outputfile",
                      type="string",
                      help="[Optional] Set output filename -- type(csv)")

    (options, args) = parser.parse_args()

    if options.inputfile is None or options.inputfile_seller is None:
      print("Type input Filename of stroy_header and story_header_sell_all")
      sys.exit(0)
    else:
      print(options)

if __name__ == '__main__':
    main()
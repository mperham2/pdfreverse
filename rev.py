from pyPdf import PdfFileWriter, PdfFileReader
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print 'test.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print 'test.py -i <inputfile> -o <outputfile>'
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
    print 'Input file is "', inputfile, '"'
    print 'Output file is "', outputfile, '"'
    output_pdf = PdfFileWriter()
    with open(inputfile, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)
        total_pages = input_pdf.getNumPages()
        for page in xrange(total_pages - 1, -1, -1):
            output_pdf.addPage(input_pdf.getPage(page))
        with open(outputfile, "wb") as writefile:
            output_pdf.write(writefile)


if __name__ == "__main__":
   main(sys.argv[1:])



#
#with open(r'12901967.pdf', 'rb') as readfile:
#    input_pdf = PdfFileReader(readfile)
#    total_pages = input_pdf.getNumPages()
#    for page in xrange(total_pages - 1, -1, -1):
#        output_pdf.addPage(input_pdf.getPage(page))
#    with open(r'output2.pdf', "wb") as writefile:
#        output_pdf.write(writefile)

#r'12901967.pdf'
#r'output.pdf'



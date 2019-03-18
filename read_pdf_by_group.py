import os
import PyPDF2
import pdf2txt
def ReadPdfsGroupByLabel(root_dir):
    """

    :param root_dir: root directory of the training pdfs
    the pdf should be grouped by label and put in a subdirectory for each label
    :return: A dictionary whose key is the label and the value is a unicode strings read from pdf
    """

    labels_to_pdfs = {}
    for sub_dir in os.listdir(root_dir):
        if sub_dir == '.DS_Store':
            continue
        if not os.path.isdir(os.path.join(root_dir,sub_dir)):
            continue

        label = sub_dir
        path = os.path.join(root_dir, sub_dir)
        unicode_strings = []
        for pdf in os.listdir(path):
            if pdf.endswith('.pdf'):
                try:
                    unicode_strings.append(pdf2txt.pdf2txt(os.path.join(path, pdf)))
                except PyPDF2.utils.PdfReadError:
                    pass
                except KeyError:
                    pass

        labels_to_pdfs[label] = unicode_strings

    return labels_to_pdfs
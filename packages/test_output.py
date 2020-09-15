# no logical unit tests available for output package
#
# Testing done outside of Python:
# ---------------------------------
#
# all output files generate correct filenames
#
# output_txt: file formatted as expected
#
# output_json: json output validated on jsonlint.com for correctness
#
# output_csv: csv file tested with LibreOffice
#
# date_format: correct datetime format outputted (did not unit test since
# time between datetime.now calls may generate different results)
#
# check_for_dir: checked within file browser, directory generated only
# when it does not exist. Tested on both Arch Linux and Windows machines

#-------------------------------------------------------------------------------
# P1 Test
# @author damienNagle
#-------------------------------------------------------------------------------
from subprocess import call

# Set the test number and then loop over the available tests
test_number = 1

# Clear the tests from the student folder
call('[ -e student/*.output ] && (rm student/*.output)', shell=True)

for i in range(1,test_number + 1):
    call('(python p1.py > student/test{0}.output) < test/test{0}.input'.format(i), shell=True)
    call('(diff student/test{0}.output test/test{0}.output && echo "Test{0} Passed") || (echo "Test{0} Failed")'.format(i), shell=True)

#!/bin/bash

# =================================================================================================== #
# Run unit tests for word_retrieve_app.
# =================================================================================================== #

# =================================================================================================== #

# =================================================================================================== #
run_test_for_hashing() {
    nosetests $nosetests_args tst/TestHashUtils.py
}

# =================================================================================================== #
run_test_for_encrypt() {
    nosetests $nosetests_args tst/TestEncryptUtils.py
}

# =================================================================================================== #
run_test_for_request() {
    nosetests $nosetests_args tst/TestRetrieveUtilsRequest.py
}

# =================================================================================================== #
run_test_for_word_parsing() {
    nosetests $nosetests_args tst/TestRetrieveUtilsWordParser.py
}

run_all_word_retrieve_tests() {
	run_test_for_hashing
	run_test_for_request
	run_test_for_word_parsing
	run_test_for_encrypt
}

# =================================================================================================== #

cleanup() {
    rm -rf nosetests.xml
}

# =================================================================================================== #

if [ $# -eq 0 ]; then    # No arguments provided. Run all unit tests.
    run_all_word_retrieve_tests
fi

cleanup

exit $coverage_exit_status

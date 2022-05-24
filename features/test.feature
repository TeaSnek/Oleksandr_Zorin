Feature: Dropbox API

    Scenario: Upload file
        Given file name is "text.txt"
        When uploading "text.txt" file to Dropbox
        Then file "text.txt" is uploaded
        
    Scenario: Get file metadata by id
        Given file named "text.txt" is uploaded
        When requesting metadata of "text.txt" by its id
        Then we receive metadata for "text.txt"
        
    Scenario: Delete file by path
        Given we have file path of "text.txt"
        When we request to delete "text.txt"
        Then file "text.txt" deleted
        
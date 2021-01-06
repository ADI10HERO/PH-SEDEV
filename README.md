### Philips Healthcare's Sierra ECG format Data Extractor and Visualizer (PH-SEDEV)

Extracts data via Node package by [Christopher Watford](christopher.watford@gmail.com), find the package [here](https://github.com/sixlettervariables/sierra-ecg-tools)


## How to Run
- Place your xml file in the directory
- Change the filename hardcoded in the index.js file or rename your XML file as "sample.xml"
-  ```sh
    (env) ~> npm i
    (env) ~> node index.js
    # check files generated in output_files directory
    (env) ~> python visualize.py
    ```

### Contributing Guide
- Fork
- Try to solve issues/TODO's
- Make PR

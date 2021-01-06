var sierraEcg = require('sierraecg');
var fs = require('fs');

filename = 'sample.xml' // path to the xml file

sierraEcg.readFile(filename, function(err, ecg) {
    if (err) {
        console.error(err);
    } else {
        console.log('Found %d leads', ecg.leads.length);
        ecg.leads
            .filter(function(lead) {
                return lead.enabled;
            }).forEach(function(lead) {
                console.log(
                    '    %s: %s ... (%d samples)',
                    lead.name,
                    lead.data.slice(0, 10).join(' '),
                    lead.data.length);
                var json_object = {
                    'data': lead.data,
                    'name': lead.name,
                    'size': lead.data.length
                }
                fs.writeFile("output_files/output_" + lead.name + ".json", JSON.stringify(json_object), function(err) {
                    if (err) throw err;
                    console.log('complete');
                });
            });
    }
});

// to run:
// node index.js
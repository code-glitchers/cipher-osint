<!DOCTYPE html>
<html>
<head>
    <title>Network Mapping</title>
    <style>
        #mynetwork {
            width: 100%;
            height: 600px;
            border: 1px solid lightgray;
        }

        .input-container {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Network Mapping</h1>

    <div class="input-container">
        <label for="node-id">Node ID:</label>
        <input type="text" id="node-id">
        <label for="node-label">Node Label:</label>
        <input type="text" id="node-label">
        <button onclick="addNode()">Add Node</button>
    </div>

    <div class="input-container">
        <label for="edge-from">From:</label>
        <select id="edge-from"></select>
        <label for="edge-to">To:</label>
        <select id="edge-to"></select>
        <button onclick="addEdge()">Add Edge</button>
    </div>

    <div id="mynetwork"></div>

    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script>
        // Network data
        var nodes = [];
        var edges = [];

        // Get input elements
        var nodeIdInput = document.getElementById('node-id');
        var nodeLabelInput = document.getElementById('node-label');
        var edgeFromSelect = document.getElementById('edge-from');
        var edgeToSelect = document.getElementById('edge-to');

        // Function to add a new node
        function addNode() {
            var id = nodeIdInput.value;
            var label = nodeLabelInput.value;

            if (id && label) {
                nodes.push({ id: id, label: label });
                nodeIdInput.value = '';
                nodeLabelInput.value = '';
                updateNetwork();
                updateEdgeSelects();
            }
        }

        // Function to add a new edge
        function addEdge() {
            var from = edgeFromSelect.value;
            var to = edgeToSelect.value;

            if (from && to) {
                edges.push({ from: from, to: to });
                updateNetwork();
            }
        }

        // Function to update the network visualization
        function updateNetwork() {
            var container = document.getElementById('mynetwork');
            var data = {
                nodes: nodes,
                edges: edges
            };
            var options = {};
            var network = new vis.Network(container, data, options);
        }

        // Function to update the edge selects with the available node options
        function updateEdgeSelects() {
            var selectOptions = '';
            for (var i = 0; i < nodes.length; i++) {
                selectOptions += '<option value="' + nodes[i].id + '">' + nodes[i].label + '</option>';
            }
            edgeFromSelect.innerHTML = selectOptions;
            edgeToSelect.innerHTML = selectOptions;
        }
    </script>
</body>
</html>

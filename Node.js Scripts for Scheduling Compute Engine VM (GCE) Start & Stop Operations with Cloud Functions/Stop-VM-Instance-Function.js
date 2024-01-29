
const Compute = require('@google-cloud/compute');
const compute = new Compute();

exports.stopGCPInstance = async (req, res) => {
  try {
    const projectId = 'akshay-000007'; // Replace with your project ID
    const zone = 'us-west1-b'; // Replace with your instance zone
    const instanceName = 'akshai-vm-stop'; // Replace with your instance name

    const zoneObj = compute.zone(zone);
    const vm = zoneObj.vm(instanceName);
    console.log('Stopping instance...');
    const [operation] = await vm.stop();
    await operation.promise();
    console.log('Instance stopped successfully.');
    res.status(200).send('Instance stopped successfully.');
  } catch (err) {
    console.error('Error during instance stop:', err);
    res.status(500).send(err);
  }
};
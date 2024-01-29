
const Compute = require('@google-cloud/compute');
const compute = new Compute();

exports.startGCPInstance = async (req, res) => {
  try {
    const projectId = 'akshay-000007'; // Replace with your project ID
    const zone = 'us-west1-b'; // Replace with your instance zone
    const instanceName = 'akshai-vm'; // Replace with your instance name

    const zoneObj = compute.zone(zone);
    const vm = zoneObj.vm(instanceName);
    console.log('Starting instance...');
    const [operation] = await vm.start();
    await operation.promise();
    console.log('Instance started successfully.');
    res.status(200).send('Instance started successfully.');
  } catch (err) {
    console.error('Error during instance start:', err);
    res.status(500).send(err);
  }
};
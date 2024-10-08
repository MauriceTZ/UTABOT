from setuptools import find_packages, setup

package_name = 'utabot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='utabot',
    maintainer_email='utabot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = utabot_controller.controller:main",
            "mpu6050_publisher = utabot_controller.mpu6050_publisher:main"
        ],
    },
)

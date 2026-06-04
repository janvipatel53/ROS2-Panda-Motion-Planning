from setuptools import find_packages, setup

package_name = 'panda_motion'

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
    maintainer='janvi',
    maintainer_email='janvi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
    'hello_node = panda_motion.hello_node:main',
    'joint_reader = panda_motion.joint_reader:main',
    'joint_monitor = panda_motion.joint_monitor:main',
    'fk_monitor = panda_motion.fk_monitor:main',
],
},
)

from setuptools import setup, find_packages

setup(
    name='cau',
    version='0.0.3',  # 版本号
    description='通过命令行进行中国农业大学的校园网认证',
    author='nyl',
    author_email='c2605759123@163.com',
    url='https://github.com/NingYuanLin/cau_auth',
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': ['cau=cau_auth.cau:main']
    },
    packages=find_packages(),
    # package_dir={'': 'cau_auth'},
    include_package_data=True,
)

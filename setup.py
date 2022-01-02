from setuptools import setup, find_packages

setup(
    name='cau',
    version='0.0.1',  # 版本号
    description='通过命令行进行中国农业大学的校园网认证',
    author='nyl',
    author_email='c2605759123@163.com',
    url='https://github.com/NingYuanLin/cau_auth',
    # py_modules=['cau'],
    entry_points={
        'console_scripts': ['cau=cau_auth.cau:main']
    },
    # packages=['src.core', 'src.helper', 'src.utils', 'statics'],
    # package_data={
    #     "cau_auth": ["statics/*"]
    # },
    packages=find_packages(),
    # package_dir={'': 'cau_auth'},
    include_package_data=True,
)

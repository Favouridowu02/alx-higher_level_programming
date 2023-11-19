#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - a function that print some basic info
 * about Python lists
 * @p: the list
 */
void print_python_list(PyObject *p)
{
        int i;

	printf("[*] Python list info\n")
        printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < Py_SIZE(p); i++)
	{
                printf("Element %d: bytes", i)
		printf("[.] bytes object info")			
	   	printf("size: %s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

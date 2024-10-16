import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {FRUIT_MODULE_DECLARATIONS, FruitRoutingModule} from  './Fruit-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    FruitRoutingModule
  ],
  declarations: FRUIT_MODULE_DECLARATIONS,
  exports: FRUIT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class FruitModule { }